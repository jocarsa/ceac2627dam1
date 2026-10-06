-- Creo un usuario tiendaestetoscopios
CREATE USER 'tiendaestetoscopios'@'localhost' IDENTIFIED BY 'TiendaEstetoscopios123$';

-- A ese usuario le pemito acceder a todo en el servidor
GRANT USAGE ON *.* TO 'tiendaestetoscopios'@'localhost';

-- A ese usuario le quito limites para que pueda hacer de todo
ALTER USER 'tiendaestetoscopios'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendaestetoscopios.* 
TO 'tiendaestetoscopios'@'localhost';

FLUSH PRIVILEGES;
