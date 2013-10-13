=========================================
Askbot installation with Vagrant + Fabric
=========================================

This repository contain my `askbot <http://askbot.org/>`_ installation script for `French « Revenu de base » website <http://revenudebase.info/>`_.

Contact : contact@stephane-klein.info

The Vagrant VM is a Debian Wheezy 64.

Instructions
============

Prerequisites :

* GNU/Linux or MacOSX
* `Python <http://www.python.org/>`_
* `Vagrant 1.2.5 or upper <http://downloads.vagrantup.com/>`_
* `Virtualbox <https://www.virtualbox.org/>`_
* Install vagrant plugins :

::

    $ vagrant plugin install vagrant-hostsupdater
    $ vagrant plugin install vagrant-hostmanager
    $ vagrant plugin install vagrant-cachier


Start
=====

::

    $ python bootstrap.py
    $ vagrant up
    $ bin/fab vagrant install


Open this url in your browesr : http://questions.revenudebase.info

Defaut admin user is :

* login : ``stephane-klein``
* password : ``password``
