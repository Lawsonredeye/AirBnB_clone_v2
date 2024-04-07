#!/usr/bin/env bash
# - script that sets up your web servers for the deployment of web_static
# - check if Nginx is installed else install if not exists

content="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"

check=$(which nginx)
if [ -z "$check" ]
then
  sudo apt update -y
	sudo apt install nginx -y
fi 

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
sudo echo "$content" > sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data

sudo sed -i 's#root /var/www/html;#root /var/www/html;\n        location /hbnb_static/ {\n            alias /data/web_static/current/;\n        }#' /etc/nginx/sites-enabled/default

# - Restart Server
sudo service nginx restart
