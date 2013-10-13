# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
if [ ! -d /root/.ssh ]
then
    sudo mkdir /root/.ssh
    sudo cp .ssh/authorized_keys /root/.ssh/
    sudo chown root:root /root/.ssh/authorized_keys
fi
SCRIPT

Vagrant.configure("2") do |config|
    config.vm.box = "debian-wheezy64"
    config.vm.box_url = "https://dl.dropboxusercontent.com/s/xymcvez85i29lym/vagrant-debian-wheezy64.box"
    config.vm.hostname = "questions.revenudebase.info"
    config.vm.provision :shell, inline: $script
    config.vm.provision :hostmanager
    config.hostmanager.enabled = true
    config.hostmanager.ignore_private_ip = false
    config.vm.network :private_network, ip: "192.168.33.12"
    config.hostsupdater.aliases = ["questions.revenudebase.info"]
    config.hostmanager.aliases = ["questions.revenudebase.info"]

    #config.vm.synced_folder "prod", "/home/vagrant/prod/", :nfs => true
end
