sudo mysql -u root -p

CREATE DATABASE miweb;
USE miweb;

CREATE TABLE contacto(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  correo VARCHAR(100),
  mensaje TEXT
);