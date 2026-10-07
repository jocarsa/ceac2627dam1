sudo mysql -u root -p

CREATE DATABASE subconsultas;

USE subconsultas;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATE,
  cliente_id INT,
  cantidad DECIMAL(4,2)
);