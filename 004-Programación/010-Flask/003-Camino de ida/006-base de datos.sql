sudo mysql -u root -p

CREATE DATABASE caminodeida;

USE caminodeida;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);
