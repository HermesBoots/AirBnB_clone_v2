# setup a web server with a link to deployed web paths

$nginx_site_config = "server {
	listen 80 default_server;
	listen [::]:80 default_server ipv6only=on;
	root /var/www/html;

	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}"

package { 'Nginx installation':
  ensure => latest,
  name   => 'nginx'
}

file { 'Nginx site configuration':
  ensure  => file,
  content => $nginx_site_config,
  path    => '/etc/nginx/sites-available/default',
  require => Package['nginx']
}

service { 'Nginx service':
  ensure    => running,
  enable    => true,
  name      => 'nginx',
  subscribe => File['/etc/nginx/sites-available/default']
}


file { 'shared resource folder':
  ensure => directory,
  group  => 'ubuntu',
  owner  => 'ubuntu',
  path   => '/data/web_static/shared'
}

file { 'site index':
  ensure  => file,
  content => 'Sample content.',
  path    => '/var/www/html/index.html'
}

file { 'test index':
  ensure  => file,
  content => 'Sample content.',
  group   => 'ubuntu',
  owner   => 'ubuntu',
  path    => '/data/web_static/releases/test/index.html'
}

file { 'link to latest deployment':
  ensure => link,
  group  => 'ubuntu',
  owner  => 'ubuntu',
  path   => '/data/web_static/current',
  target => '/data/web_static/releases/test'
}
