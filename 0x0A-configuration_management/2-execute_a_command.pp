# terminates a program after executing a command from puppet
exec { 'kill_me_now':
  command => ['/usr/bin/pkill', 'killmenow'],
  onlyif  => 'pgrep killmenow',
}
