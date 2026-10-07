sudo mysql -u root -p

CREATE DATABASE tiendaestetoscopios;

USE tiendaestetoscopios;

CREATE TABLE estetoscopios(
 id INT PRIMARY KEY AUTO_INCREMENT,
 nombre VARCHAR(100),
 descripcion TEXT,
 precio DECIMAL(4,2)
);