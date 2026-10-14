CREATE TABLE datos_personales(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE datos_contacto(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  email VARCHAR(100),
  telefono VARCHAR(100)
);

CREATE TABLE redes_sociales(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  linkedin VARCHAR(100),
  facebook VARCHAR(100),
  instagram VARCHAR(100),
  github VARCHAR(100)
);

CREATE TABLE experiencias_laborales(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  empresa VARCHAR(100),
  descripcion TEXT,
  cargo VARCHAR(100),
  inicio VARCHAR(100),
  final VARCHAR(100)
);

CREATE TABLE formacion(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  centro VARCHAR(100),
  descripcion TEXT,
  titulo VARCHAR(100),
  inicio VARCHAR(100),
  final VARCHAR(100)
);

CREATE TABLE idiomas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  idioma VARCHAR(100),
  nivel VARCHAR(100)
);

