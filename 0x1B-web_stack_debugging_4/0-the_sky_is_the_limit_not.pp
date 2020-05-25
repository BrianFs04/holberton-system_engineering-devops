# Fix the limit of request by default
exec { 'fix--for-nginx':
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
  provider => 'shell'
}