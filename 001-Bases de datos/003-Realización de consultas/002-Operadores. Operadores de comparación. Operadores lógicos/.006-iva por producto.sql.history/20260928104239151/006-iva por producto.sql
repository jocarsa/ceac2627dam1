SELECT 
nombre,
precio AS 'Base imponible',
precio*0.21 AS 'IVA',
precio + precio*0.21 AS 'Total'
FROM productos;