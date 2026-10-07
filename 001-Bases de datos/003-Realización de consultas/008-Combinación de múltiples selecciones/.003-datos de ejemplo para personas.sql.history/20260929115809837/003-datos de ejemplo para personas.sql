INSERT INTO personas 
(nombre, apellidos, email, salario, fecha_contratacion, departamento_id, jefe_id) 
VALUES
-- Algunos registros conservados de empleados
('Ana', 'García López', 'ana@empresa.com', 32000, '2018-03-15', 1, NULL),
('Carlos', 'Martínez Pérez', 'carlos@empresa.com', 28000, '2020-06-01', 1, 1),
('Pedro', 'Gómez Torres', 'pedro@empresa.com', 35000, '2017-01-10', 2, NULL),
('Marta', 'Navarro Gil', 'marta@empresa.com', 24000, '2021-04-12', 2, 4),
('Javier', 'Vidal Serra', 'javier@empresa.com', 31000, '2016-09-01', 3, NULL),
('Sofía', 'Castro Vega', 'sofia@empresa.com', 38000, '2018-05-21', 4, NULL),
('Miguel', 'Fuentes Lara', 'miguel@empresa.com', 33000, '2015-04-17', 5, NULL),
('Fernando', 'Blasco Puig', 'fernando@empresa.com', 42000, '2014-06-01', 7, NULL),

-- Registros nuevos
('María', 'López Ferrer', 'maria@empresa.com', 27500, '2021-05-14', 1, 1),
('Roberto', 'Jiménez Alba', 'roberto@empresa.com', 30500, '2020-02-20', 2, 4),
('Patricia', 'Domínguez Gil', 'patricia@empresa.com', 25500, '2022-09-12', 3, 8),
('Alejandro', 'Muñoz Pérez', 'alejandro@empresa.com', 36000, '2019-07-01', 4, 11),
('Beatriz', 'Serrano Vidal', 'beatriz@empresa.com', 24500, '2023-01-18', 5, 14),
('Héctor', 'Rubio Torres', 'hector@empresa.com', 31500, '2020-11-23', 6, 16),
('Irene', 'Calvo Martínez', 'irene@empresa.com', 29000, '2022-04-07', 7, 18),
('Daniel', 'Pascual Romero', 'daniel@empresa.com', 22500, '2024-02-15', 1, 1),
('Eva', 'Méndez Navarro', NULL, 23500, '2024-06-10', 2, 4),
('Óscar', 'Gallego Ruiz', 'oscar@empresa.com', 28500, '2023-10-02', 3, 8);