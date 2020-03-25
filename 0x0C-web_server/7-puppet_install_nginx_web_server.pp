# Install Nginx web-server using puppet
exec { 'installNginx':
  command  =>  'sudo apt-get -y update ;sudo apt-get -y install nginx ; echo "Holberton School" > sudo tee /var/www/html/index.nginx-debian.html ; sed -i "s/server_name _;/\n\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-avaliable/default ; sudo service nginx start',
  provider =>  shell
}