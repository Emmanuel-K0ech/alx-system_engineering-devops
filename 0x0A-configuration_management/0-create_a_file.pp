# This script creates a file in /tmp with the following atributes
# path, permission, owner, group and file contents

file {'/tmp/school':
    path    => '/tmp/school',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
    }
