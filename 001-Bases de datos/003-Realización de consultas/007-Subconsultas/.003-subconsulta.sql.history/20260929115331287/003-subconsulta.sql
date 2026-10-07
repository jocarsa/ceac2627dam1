SELECT 
nombre,
precio,
precio > (
	SELECT AVG(precio) FROM productos
) AS 'media'
FROM productos;