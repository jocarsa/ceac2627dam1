CREATE TABLE datos_contacto(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  email VARCHAR(100),
  telefono VARCHAR(100)
);

INSERT INTO datos_contacto VALUES(
	NULL,
  1,
  'info@jocarsa.com',
  '620891718'
);

SELECT * FROM datos_contacto;