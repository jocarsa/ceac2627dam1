CREATE USER 'tiendaestetoscopios'@'localhost' IDENTIFIED BY 'TiendaEstetoscopios123$';

GRANT USAGE ON *.* TO 'tiendaestetoscopios'@'localhost';

ALTER USER 'tiendaestetoscopios'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendaestetoscopios.* 
TO 'tiendaestetoscopios'@'localhost';

FLUSH PRIVILEGES;
