Deberíamos tener:

1.-Tabla de clientes:
CREATE TABLE Clientes (
    Nombre VARCHAR(100),
    Apellidos VARCHAR(100),
    Telefono VARCHAR(25),
    Email VARCHAR(100)
);

2.-Tabla de productos
CREATE TABLE Productos(
	nombre VARCHAR(100),
  precio DECIMAL(6,2)
);

3.-Tabla de pedidos:
CREATE TABLE Pedidos(
	fecha DATE,
  numero_de_pedido INT,
  cliente_id INT,
  producto_id INT
);