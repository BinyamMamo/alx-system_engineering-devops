# terminates a program after executing a command from puppet
package { 'pgrep':
  ensure => installed,
}
package { 'pkill':
  ensure => installed,
}
exec { 'kill_me_now':
  command => ['/usr/bin/pkill', 'killmenow'],
  onlyif  => 'pgrep killmenow',
}
