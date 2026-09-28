SELECT 
nombre,
precio AS 'Base imponible',
precio*0.21 AS 'IVA',
precio*1.21 AS 'Total'
FROM productos;