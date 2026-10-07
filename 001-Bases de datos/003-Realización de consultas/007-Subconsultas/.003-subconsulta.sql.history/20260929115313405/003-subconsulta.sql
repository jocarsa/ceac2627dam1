SELECT 
nombre,
precio,
precio > (
	SELECT AVG(precio) FROM productos
)
FROM productos;