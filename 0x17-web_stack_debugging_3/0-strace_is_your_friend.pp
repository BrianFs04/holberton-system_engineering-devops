# Using strace to find the error in apache2
exec { 'StraceFix':
  command  => 'sudo mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  provider => shell,
}