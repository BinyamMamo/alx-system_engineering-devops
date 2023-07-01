# installs the flask package(version 2.1.0) using puppet
package { 'flask':
  ensure  => '2.1.0',
  provide => 'pip3',
}
