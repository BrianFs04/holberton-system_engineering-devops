# Install Nginx web-server using puppet
exec { 'installNginx':
  $part1 = "sudo apt-get -y install nginx ; echo \"Holberton School\" | sudo tee /var/www/html/index.nginx-debian.html",
  $mycommand = "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/",
  command  =>  'sudo apt-get -y update ; $part1 ;  sudo sed -i "$mycommand" /etc/nginx/sites-avaliable/default ; sudo service nginx start',
  provider =>  shell,
}