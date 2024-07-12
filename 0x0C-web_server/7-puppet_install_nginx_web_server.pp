# Puppet configure nginx with custom 404 page and redirect

# Add stable version of nginx repository
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository -y ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => 'grep -r "deb .*nginx/stable" /etc/apt/sources.list*',
}

# Update the software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => Exec['add nginx stable repo'],
}

# Install nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update packages'],
}

# Allow HTTP traffic through firewall
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => "ufw status | grep 'Nginx HTTP'",
}

# Ensure proper permissions for the web root directory
file { '/var/www':
  ensure  => directory,
  mode    => '0755',
  recurse => true,
}

# Create index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
  mode    => '0644',
}

# Create custom 404 error page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
  mode    => '0644',
}

# Configure Nginx default site
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure Nginx is running and restart if configuration changes
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}
