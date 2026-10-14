sudo mysql -u root -p

CREATE DATABASE blogceac2627;

USE blogceac2627;

CREATE TABLE articulos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(100),
  fecha DATE,
  contenido TEXT
);
