1.-Abrís terminal (de Linux, no de MySQL) - si hace falta, exit;

2.-Ponéis esto:
mysqldump -u root -p [tubasededatos] > copiadeseguridad.sql

3.-Por ejemplo:
sudo mysqldump -u root -p empresadam2627 > copiadeseguridad.sql

4.-Acabáis de hacer una copia de seguridad y eso es SAGRADO

