CREATE USER 'tiendacalzado'@'localhost' IDENTIFIED BY 'TiendaCalzado123$';

GRANT USAGE ON *.* TO 'tiendacalzado'@'localhost';

ALTER USER 'tiendacalzado'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendacalzados.* 
TO 'tiendacalzado'@'localhost';

FLUSH PRIVILEGES;
