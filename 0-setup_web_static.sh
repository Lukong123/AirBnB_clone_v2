#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y

#create folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

#HTML file
echo "Holberton By Dlhz" > /data/web_static/releases/test/index.html

#Symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#Set ownership
sudo chown -R ubuntu:ubuntu /data/

#Nginx config
sudo sed -i "38i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
