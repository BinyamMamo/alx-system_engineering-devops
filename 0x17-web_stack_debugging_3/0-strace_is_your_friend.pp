# substitutes phpp with php to fix a wordpress issue

exec { 'fixing a wordpress server':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider =>  shell,
}

