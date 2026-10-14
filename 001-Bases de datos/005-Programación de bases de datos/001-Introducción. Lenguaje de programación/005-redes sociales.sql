CREATE TABLE redes_sociales(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  linkedin VARCHAR(100),
  facebook VARCHAR(100),
  instagram VARCHAR(100),
  github VARCHAR(100)
);

INSERT INTO redes_sociales VALUES(
	NULL,
  1,
  "https://linkedin.com/in/jvcarratala",
  "https://facebook.com/carratala",
  "https://instagram.com/jvcarratala",
  "https://github.com/jocarsa"
);

SELECT * FROM redes_sociales;