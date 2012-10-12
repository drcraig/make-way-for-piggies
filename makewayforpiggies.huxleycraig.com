# Place any notes or comments you have here
# It will make any customisation easier to understand in the weeks to come

<VirtualHost *:80>

  # Admin email, Server Name (domain name) and any aliases
  ServerAdmin drcraig@alum.mit.edu
  ServerName  makewayforpiggies.huxleycraig.com

  # Index file and Document Root (where the public files are located)
  DirectoryIndex index.html
  DocumentRoot /home/drcraig/public_html/makewayforpiggies.huxleycraig.com/public


  # Custom log file locations
  LogLevel warn
  ErrorLog  /home/drcraig/public_html/makewayforpiggies.huxleycraig.com/log/error.log
  CustomLog /home/drcraig/public_html/makewayforpiggies.huxleycraig.com/log/access.log combined

  <Directory /home/drcraig/public_html/makewayforpiggies.huxleycraig.com/public>
    Options FollowSymLinks
  </Directory>

</VirtualHost>
