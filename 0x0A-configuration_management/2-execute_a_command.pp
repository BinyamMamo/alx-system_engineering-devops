# terminates a program after executing a command from puppet
package { 'pgrep':
  ensure => installed,
}
package { 'pkill':
  ensure => installed,
}
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path => '/usr/bin/:/usr/local/bin/:/bin/',
  onlyif  => 'pgrep killmenow',
}
