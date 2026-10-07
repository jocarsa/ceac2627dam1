sudo mysql -u root -p

CREATE DATABASE tratamiento;

USE tratamiento;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO INCREMENT,
	nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);