CREATE USER 'tiendacalzado'@'localhost' IDENTIFIED BY 'TiendaCalzado123$';

GRANT USAGE ON *.* TO 'tiendacalzado'@'localhost';



ALTER USER 'tiendacalzado'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON [tubasededatos].* 
TO '[tunombredeusuario]'@'[tuservidor]';

GRANT ALL PRIVILEGES ON empresadam2627.* 
TO 'josevicente2627'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
