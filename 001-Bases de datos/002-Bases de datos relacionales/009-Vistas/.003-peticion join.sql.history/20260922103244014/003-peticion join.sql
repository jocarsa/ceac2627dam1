SELECT 
Pedidos.fecha,
Pedidos.numero_de_pedido,
Clientes.nombre,
Clientes.apellidos,
Productos.nombre
FROM Pedidos
LEFT JOIN Clientes ON Pedidos.cliente_id = Clientes.Identificador
LEFT JOIN Productos ON Pedidos.producto_id = Clientes.Identificador;