#!/usr/bin/env bash

# install nginx if bit exiting in os
nb=$(which nginx | wc -l)
if [ $nb -eq 0 ]
then
    echo "nginx is not installed"
    echo "installation of the nginx server"
    sudo apt-get update -y
    sudo apt-get install nginx -y
else
    echo "nginx installé"
fi

sudo rm -rf /data
echo "creation of directories"
sudo mkdir -p -v /data/web_static/releases/
sudo mkdir -p -v /data/web_static/shared/
sudo mkdir -p -v /data/web_static/releases/test/
#echo "Hello World Nginx" > index.html
#sudo mv index.html /data/web_static/releases/test/
#cat /data/web_static/releases/test/index.html

echo "creation of the symbolic link"
sudo rm /data/web_static/current
sudo ln -s -v /data/web_static/releases/test/ /data/web_static/current

echo "Give ownership of the /data/ folder to the ubuntu user AND group"
USER=$('whoami')
sudo chown -R $USER:ubuntu /data
ls -l /data

echo "cloning of the deposit AirBnB_Clone"
git clone https://github.com/HamaBarhamou/AirBnB_clone_v2.git airb
echo "Copy web_static in data path"
sudo mv airb/web_static /data/web_static/releases/test
echo "Delete a repository"
rm -rf airb

echo "Configuration a server ngnix"

SERVER_CONFIG=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /data/web_static/current/web_static;
	index index.html index.htm index.nginx-debian.html 103-index.html;
	server_name _;
	location / {
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me){
		rewrite ^ https://hamabarhamou.github.io/monCV/ permanent;
	}
}"

echo -e $SERVER_CONFIG > default
#sudo cp /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default_save
sudo mv default /etc/nginx/sites-enabled/
ls /etc/nginx/sites-enabled

if [ "$(pgrep -c nginx)" -le 0 ]; then
    echo "start of ngnix"
	sudo service nginx start
else
    echo "restart of ngnix"
	sudo service nginx restart
fi