sudo mysql -u root -p

CREATE DATABASE clase;
USE clase;
SHOW TABLES;

CREATE TABLE alumnos (
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    fecha_de_nacimiento VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(100)
);
SHOW TABLES;
DESCRIBE alumnos;