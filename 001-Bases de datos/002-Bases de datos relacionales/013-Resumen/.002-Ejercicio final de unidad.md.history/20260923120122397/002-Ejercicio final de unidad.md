Subunidad 1:
Ejemplo:
Alumno
	-nombre
  -apellidos
  -fecha_de_nacimiento
  -email
  -telefono


Subunidad 2:
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
SELECT * FROM alumnos;

Subunidad 5:
ALTER TABLE alumnos
ADD CONSTRAINT chk_clientes_email
CHECK (
    email IS NULL
    OR email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
);

Subunidad 6: (nos la saltamos)

Subunidad 7: Claves ajenas
