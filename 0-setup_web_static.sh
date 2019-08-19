#!/usr/bin/env bash
# install directories on remote server for serving web releases

apt-get update
apt-get --yes install nginx
mkdir --parents /data/web_static/releases/test
mkdir --parents /data/web_static/shared
ln --force --symbolic /data/web_static/releases/test /data/web_static/current
cat > /data/web_static/releases/test/index.html << EOF
<!DOCTYPE html>
<html>
<head>
	<title>Fabric Test</title>
</head>
<body>
	<p>Nothing for now.</p>
</body>
</html>
EOF
chown --recursive ubuntu:ubuntu /data
cat > /etc/nginx/sites-available/default << EOF
server {
	listen 80 default_server;
	listen [::]:80 default_server ipv6only=on;
	root /var/www/html;
	index index.html;

	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}
EOF
service 'nginx' reload
service 'nginx' restart
