SELECT 
pedidos.fecha,
pedidos.cantidad,
clientes.nombre,
clientes.apellidos
FROM pedidos
LEFT JOIN clientes
ON pedidos.cliente_id = clientes.id;