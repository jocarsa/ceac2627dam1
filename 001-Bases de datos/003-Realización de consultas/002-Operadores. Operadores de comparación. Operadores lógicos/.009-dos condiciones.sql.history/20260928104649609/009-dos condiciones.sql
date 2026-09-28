SELECT 
nombre,
precio AS 'Base imponible',
precio*0.21 AS 'IVA',
precio + precio*0.21 AS 'Total',
precio < 500 AS 'Barato',
precio > 500 AND nombre = 'Portátil Basic'
FROM productos;