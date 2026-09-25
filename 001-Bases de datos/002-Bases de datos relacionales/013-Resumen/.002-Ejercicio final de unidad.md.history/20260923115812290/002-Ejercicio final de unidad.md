Subunidad 1:
sudo mysql -u root -p

CREATE DATABASE clase;
USE clase;
SHOW TABLES;

Subunidad 3:
CREATE TABLE alumnos (
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    fecha_de_nacimiento VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(100)
);
SHOW TABLES;
DESCRIBE alumnos;

Subunidad 4:
ALTER TABLE alumnos
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;
DESCRIBE alumnos;
INSERT INTO alumnos VALUES(
	'Jose Vicente',
  'Carratalá Sanchis',
  '1978-04-14',
  '535252354',
  'info@jocarsa.com',
  NULL
);

