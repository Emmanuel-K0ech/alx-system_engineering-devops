# This script installs flask from pip3

# Ensure pip3 is installed
package { 'python3-pip':
    ensure => present,
}

# Install flask using pip3
exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
}
