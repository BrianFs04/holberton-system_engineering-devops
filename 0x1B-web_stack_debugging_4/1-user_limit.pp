# OS configuration for holberton user
exec { 'change-os-configuration-for-holberton-user':
  environment => ['FILE=/etc/security/limits.conf',
      'HARD=hard nofile', 'SOFT=soft nofile'],
  command     => 'sudo sed -i "s/$HARD 5/$HARD 40000/g" $FILE;sudo sed -i "s/$SOFT 4/$SOFT 20000/g" $FILE; sudo sysctl -p',
  provider    => 'shell',
}