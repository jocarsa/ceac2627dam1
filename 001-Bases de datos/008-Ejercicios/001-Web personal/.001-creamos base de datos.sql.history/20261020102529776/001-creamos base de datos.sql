sudo mysql -u root -p

CREATE DATABASE miweb;
USE miweb;

--esta tabla será para escribir
CREATE TABLE contacto(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  correo VARCHAR(100),
  mensaje TEXT
);

--esta tabla será para leer
CREATE TABLE proyectos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  fecha DATE,
  descripcion TEXT,
  imagen VARCHAR(100)
);