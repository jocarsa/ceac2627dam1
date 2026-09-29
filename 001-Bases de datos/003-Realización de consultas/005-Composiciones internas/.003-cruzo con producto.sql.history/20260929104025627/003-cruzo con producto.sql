SELECT
productos.nombre,
productos.precio
ventas.cantidad,
ventas.fecha

FROM ventas

LEFT JOIN
productos ON ventas.producto_id = productos.id;