SELECT 
nombre,
MAX(precio)
FROM productos
GROUP BY precio;