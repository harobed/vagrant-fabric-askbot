import os

from fabric.api import task, local, run, env, put, settings, hide, cd  # NOQA
import fabtools

here = os.path.abspath(os.path.dirname(__file__))


def _settings_dict(config):
    _settings = {}

    # Build host string
    _settings['user'] = config['User']
    _settings['hosts'] = [config['HostName']]
    _settings['port'] = config['Port']

    # Strip leading and trailing double quotes introduced by vagrant 1.1
    _settings['key_filename'] = config['IdentityFile'].strip('"')

    _settings['forward_agent'] = (config.get('ForwardAgent', 'no') == 'yes')
    _settings['disable_known_hosts'] = True

    return _settings


def ssh_config(name=''):
    """
    Get the SSH parameters for connecting to a vagrant VM.
    """
    with settings(hide('running')):
        output = local('vagrant ssh-config %s' % name, capture=True)

    config = {}
    for line in output.splitlines()[1:]:
        key, value = line.strip().split(' ', 2)
        config[key] = value
    return config


def _add_user(*args, **kwargs):
    fabtools.require.user(*args, **kwargs)
    if 'name' not in kwargs:
        user = args[0]
    else:
        user = kwargs['name']

    if not fabtools.files.is_file('/home/%s/.ssh/authorized_keys' % user):
        run('mkdir -p /home/%s/.ssh/' % user)
        run('cp /root/.ssh/authorized_keys /home/%s/.ssh/' % user)
        run('chown %(user)s:%(user)s /home/%(user)s/.ssh/ -R' % {'user': user})


@task
def vagrant(name=''):
    config = ssh_config(name)
    extra_args = _settings_dict(config)
    env.update(extra_args)
    env['user'] = 'root'
    env['askbot_user'] = 'vagrant'


@task
def install():
    fabtools.deb.update_index()
    fabtools.deb.upgrade()
    fabtools.deb.install([
        'python', 'python-dev', 'python-pip', 'python-virtualenv',
        'git', 'postgresql-9.1', 'postgresql-server-dev-9.1',
        'memcached', 'supervisor', 'nginx', 'postfix'
    ])
    run('pip install -U pip virtualenv')
    if not fabtools.postgres.user_exists('askbot'):
        fabtools.postgres.create_user('askbot', password='password')

    if not fabtools.postgres.database_exists('askbot'):
        fabtools.postgres.create_database('askbot', owner='askbot')

    if env['askbot_user'] != 'vagrant':
        _add_user(
            name='askbot',
            password=None,
            shell='/bin/bash'
        )

    askbot_home = '/home/%s/prod/' % env['askbot_user']
    with settings(user=env['askbot_user']):
        run('echo "localhost:5432:askbot:askbot:password" > ~/.pgpass')
        run('chmod 0600 ~/.pgpass')
        run('mkdir -p %s' % askbot_home)
        with cd(askbot_home):
            run('virtualenv .')
            run('git clone https://github.com/harobed/askbot-devel.git')
            run('cd askbot-devel && ../bin/python setup.py develop')
            run('bin/pip install psycopg2 gunicorn python-memcached')

            run('bin/askbot-setup -n . -e 1 -d askbot -u askbot -p password')

            fabtools.files.upload_template(
                '%ssettings.py' % askbot_home,
                os.path.join(here, 'assets/settings.py')
            )
            run('bin/python manage.py syncdb --all --noinput')
            run('bin/python manage.py migrate --all --fake')
            run('bin/python manage.py collectstatic  --noinput')
            run('bin/python manage.py add_askbot_user --email=contact@stephane-klein.info --password=password --user-name=stephane-klein')
            run('bin/python manage.py add_admin 1 --noinput')

        put('assets/askbot/media/style/style.css', '/home/vagrant/prod/static/default/media/style/style.css')

    fabtools.require.supervisor.process(
        'askbot_prod',
        command='%sbin/python manage.py run_gunicorn -b unix:/tmp/askbot_prod.sock' % askbot_home,  # NOQA
        directory=askbot_home,
        user=env['askbot_user'],
        stdout_logfile='%sprod.log' % askbot_home,
    )

    fabtools.require.nginx.site(
        'questions.revenudebase.info',
        template_contents="""
server {
        listen 80;
        server_name %(server_name)s;

        location ~ /m(.*) {
            alias %(askbot_home)sstatic$1;
        }

        location ~ /upfiles(.*) {
            alias %(askbot_home)saskbot/upfiles$1;
        }

        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_pass http://unix:/tmp/askbot_prod.sock:/;
        }
}
""",
        enabled=True,
        askbot_home=askbot_home
    )

    # init default configuration value

    with settings(user=env['askbot_user']):
        put('assets/livesettings_setting.sql', '/tmp/')
        put('assets/livesettings_longsetting.sql', '/tmp/')

        run('psql -U askbot -h localhost -d askbot -c "delete from livesettings_setting;"')
        run('psql -U askbot -h localhost -d askbot -c "delete from livesettings_longsetting;"')
        run('psql -U askbot -h localhost -d askbot -f /tmp/livesettings_setting.sql')
        run('psql -U askbot -h localhost -d askbot -f /tmp/livesettings_longsetting.sql')
