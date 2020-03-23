#Execute a command
exec { 'kill':
  command  => 'pkill killmenow',
  provider => 'shell'
}