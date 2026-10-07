Deberíamos tener:

1.-Tabla de clientes:
CREATE TABLE Clientes (
    Nombre VARCHAR(100),
    Apellidos VARCHAR(100),
    Telefono VARCHAR(25),
    Email VARCHAR(100)
);
ALTER TABLE Clientes
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;

2.-Tabla de productos
CREATE TABLE Productos(
	nombre VARCHAR(100),
  precio DECIMAL(6,2)
);
ALTER TABLE Productos
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;

3.-Tabla de pedidos:
CREATE TABLE Pedidos(
	fecha DATE,
  numero_de_pedido INT,
  cliente_id INT,
  producto_id INT
);
ALTER TABLE Pedidos
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;