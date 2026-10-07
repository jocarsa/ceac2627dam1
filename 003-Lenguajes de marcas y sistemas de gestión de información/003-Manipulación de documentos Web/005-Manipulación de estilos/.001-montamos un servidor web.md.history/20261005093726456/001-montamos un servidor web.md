La via Linux
1.-Tenemos que estar dentro de la máquina virtual
2.-Abrimos terminal
3.-sudo apt install apache2
4.-La carpeta de publicación estará en /var/www/html
(donde deberéis trabajar a partir de este momento)
5.-PERO esa carpeta no tiene permisos
6.-PAra darle permisos, en el terminal:
7.-sudo chmod 777 -R /var/www/html
8.-A partir de este momento vuestros ejercicios deberán estar en esa carpeta

9.-Deberéis acceder poniendo en el navegador http://localhost/[carpeta]

La via Windows:
1.-Descargáis e instaláis XAMPP: https://www.apachefriends.org/es/index.html
2.-La carpeta de publicación es: C:/xampp/htdocs
3.-A partir de este momento accederéis  en http://localhost/[carpeta]