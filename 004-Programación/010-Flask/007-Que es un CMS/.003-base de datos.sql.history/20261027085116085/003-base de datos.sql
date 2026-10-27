sudo mysql -u root -p

CREATE DATABASE blogceacdam2627;

USE blogceacdam2627;

CREATE TABLE articulos (
	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(255),
  fecha DATE,
  contenido TEXT
);

