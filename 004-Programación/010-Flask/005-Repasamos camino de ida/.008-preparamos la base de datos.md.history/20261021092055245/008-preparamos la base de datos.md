sudo mysql -u root -p

CREATE DATABASE medicos;
USE medicos;

CREATE TABLE medicos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  especialidad VARCHAR(100),
  numero_de_colegiado VARCHAR(100)
);