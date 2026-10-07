SELECT 
Pedidos.fecha,
Pedidos.numero_de_pedido,
Clientes.nombre AS 'nombre del cliente',
Clientes.apellidos,
Productos.nombre AS 'nombre del producto'
FROM Pedidos
LEFT JOIN Clientes ON Pedidos.cliente_id = Clientes.Identificador
LEFT JOIN Productos ON Pedidos.producto_id = Productos.Identificador;