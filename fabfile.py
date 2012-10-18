from fabric.api import *
from fabric.contrib.project import rsync_project

env.use_ssh_config = True

def upload_files():
    rsync_project('~/public_html/makewayforpiggies.huxleycraig.com/public',
                  local_dir="build/",
                  exclude=["*.aux", "*.log", "*.toc", ".*"],
                  delete=True)

@hosts('cilantro')
def init():
    run('mkdir -p ~/public_html/makewayforpiggies.huxleycraig.com/{public,log}')
    put('makewayforpiggies.huxleycraig.com', '/etc/apache2/sites-available/', use_sudo=True)
    sudo('a2ensite makewayforpiggies.huxleycraig.com')
    upload_files()
    sudo('/etc/init.d/apache2 reload')

@hosts('cilantro')
def deploy():
    put('makewayforpiggies.huxleycraig.com', '/etc/apache2/sites-available/', use_sudo=True)
    upload_files()
    sudo('/etc/init.d/apache2 reload')
    
