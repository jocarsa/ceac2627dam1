sudo mysql -u root -p

CREATE DATABASE tiendacalzados;

USE tiendacalzados;

CREATE TABLE calzados(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion VARCHAR(255),
  precio DECIMAL(4,2)
);