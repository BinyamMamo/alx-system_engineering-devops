# installs the flask package(version 2.1.0) using puppet
package { 'python3':
  ensure   => '3.8.10',
}
package { 'python3-pip':
  ensure   => installed,
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
