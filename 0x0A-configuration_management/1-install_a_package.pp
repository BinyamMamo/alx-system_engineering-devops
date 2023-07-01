# installs the flask package(version 2.1.0) using puppet
package { 'python3-pip':
  ensure => installed,
}

package { 'python3-setuptools':
  ensure => installed,
}

package { 'python3-wheel':
  ensure => installed,
}

package { 'python3-dev':
  ensure => installed,
}

package { 'build-essential':
  ensure => installed,
}

package { 'libssl-dev':
  ensure => installed,
}

package { 'libffi-dev':
  ensure => installed,
}

package { 'python3-cffi':
  ensure => installed,
}

package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

