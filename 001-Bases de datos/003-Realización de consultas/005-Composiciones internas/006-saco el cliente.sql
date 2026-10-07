SELECT

productos.nombre AS 'nombre',
productos.precio AS 'precio',

ventas.cantidad AS 'unidades',
ventas.cantidad * productos.precio AS 'total',
ventas.fecha AS 'fecha',

empleados.nombre,
empleados.apellidos,

clientes.nombre

FROM ventas

LEFT JOIN productos ON ventas.producto_id = productos.id
LEFT JOIN empleados ON ventas.empleado_id = empleados.id
LEFT JOIN clientes ON ventas.cliente_id = clientes.id;