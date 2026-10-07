SELECT

productos.nombre AS 'nombre',
productos.precio,
ventas.cantidad,
ventas.cantidad * productos.precio
ventas.fecha

FROM ventas

LEFT JOIN productos ON ventas.producto_id = productos.id;