#!/usr/bin/env bash
# set up web static

apt-get -y update ; apt-get install -y nginx

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
chown -R ubuntu /data/ ; chgrp -R ubuntu /data/

echo "
events {}
http {
    server {
    	   listen 80 default_server;
    	   listen [::]:80 default_server;

    	   location /hbnb_static {
           	    alias /data/web_static/current;
           	    index index.html;
    	   }

}
}

" > /etc/nginx/sites-available/default

service nginx restart
nginx -s reload
