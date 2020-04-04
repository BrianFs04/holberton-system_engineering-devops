# Add a custom HTTP header with Puppet
exec { 'CustomHeader':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx; sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-available/default ; sudo service nginx start',
  provider => shell,
}