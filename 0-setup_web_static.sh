#!/usr/bin/env bash
# set up web static

apt-get -y update ; apt-get -y install nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shares/
mkdir -p /data/web_static/releases/test/

echo "
<html>
     <head>
	<title>Nginx is working</title>
     </head>
     <body>
	<h2>Nginx is working successfully</h2>
     </body>
</html>" > /data/web_static/releases/test/

if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

#giving ownership
sudo chown -R ubuntu:ubuntu /data/

echo "
events {}
http {
    server {
    	   listen 80;
    	   server_name onetarek.tech;

    	   location /hbnb_static/ {
           	    alias /data/web_static/current/;
           	    index index.html;
    	   }

}
}

" > /etc/nginx/nginx.conf

service nginx restart
nginx -s reload
