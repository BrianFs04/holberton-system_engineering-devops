# OS configuration for holberton user
exec { 'change-os-configuration-for-holberton-user':
  command  => 'sudo sed -i "s/hard nofile 5/hard nofile 40000/g" /etc/security/limits.conf;sudo sed -i "s/soft nofile 4/soft nofile 20000/g" /etc/security/limits.conf; sudo sysctl -p',
  provider => 'shell',
}