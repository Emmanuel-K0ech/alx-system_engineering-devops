#!/usr/bin/pup
# Ensure pip3 is installed and manage the package
package { 'python3-pip':
  ensure => installed,
}

# Ensure the specific version of Flask is installed using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}
