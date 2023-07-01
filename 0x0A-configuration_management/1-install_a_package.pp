# installs the flask package(version 2.1.0) using puppet
package { 'Flask':
  ensure  => '2.1.0',
  provide => 'pip3',
}
