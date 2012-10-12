from fabric.api import *
from fabric.contrib.project import rsync_project

env.use_ssh_config = True

def upload_files():
    put('index.html', '~/public_html/makewayforpiggies.huxleycraig.com/public/')
    put('style.css', '~/public_html/makewayforpiggies.huxleycraig.com/public/')
    put('jquery-1.8.2.min.js', '~/public_html/makewayforpiggies.huxleycraig.com/public/')
    put('paginate.js', '~/public_html/makewayforpiggies.huxleycraig.com/public/')
    put('jquery.event.swipe.js', '~/public_html/makewayforpiggies.huxleycraig.com/public/')
    put('jquery.event.move.js', '~/public_html/makewayforpiggies.huxleycraig.com/public/')
    put('fonts/', '~/public_html/makewayforpiggies.huxleycraig.com/public/')
    put('MakeWayForPiggies.pdf', '~/public_html/makewayforpiggies.huxleycraig.com/public/')
    run('mkdir -p ~/public_html/makewayforpiggies.huxleycraig.com/public/manual')
    put('manual/*.jpg', '~/public_html/makewayforpiggies.huxleycraig.com/public/manual/')

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
    
