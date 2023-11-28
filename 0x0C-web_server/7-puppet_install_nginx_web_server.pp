# installs and configures nginx

exec { 'apt-update':
  command     => 'apt-get update',
  path        => '/usr/bin',
  refreshonly => true
}

package { 'nginx':
  ensure => installed
}

class { 'ufw':
  allow  => ['ssh', 'http', 'Nginx HTTP'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World'
}

file { '/etc/nginx/sites-available/redirect':
  ensure  => file,
  content => "server {
                listen 80;
                server_name _;
                location /redirect_me {
                  return 301 /;
                }
              }"
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
                listen 80;
                server_name _;
                location / {
                  root /var/www/html;
                  index index.html;
                }
              }"
}

file { '/etc/nginx/sites-enabled/redirect':
  ensure  => link,
  target  => '/etc/nginx/sites-available/redirect',
  require => File['/etc/nginx/sites-available/redirect']
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default']
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [File['/etc/nginx/sites-enabled/redirect'], File['/etc/nginx/sites-enabled/default']]
}
