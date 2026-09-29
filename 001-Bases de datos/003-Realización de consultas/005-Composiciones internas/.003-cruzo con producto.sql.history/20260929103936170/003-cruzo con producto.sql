SELECT
producto_id,
cantidad,
fecha
FROM ventas
LEFT JOIN
productos ON ventas.producto_id = productos.;