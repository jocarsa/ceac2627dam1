sudo mysql -u root -p

CREATE DATABASE encuentrame;

USE encuentrame;

CREATE TABLE facultativos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100),
  n_colegiado VARCHAR(100)
);