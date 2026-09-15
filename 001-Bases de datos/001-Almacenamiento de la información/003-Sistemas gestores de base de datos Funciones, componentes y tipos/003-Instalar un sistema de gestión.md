1.-Tenemos que estar en Ubuntu
2.-Abrimos Terminal (Control + Alt + T)
3.-Actualizamos paquetes: sudo apt update
4.-Ponemos: sudo apt install mysql-server
5.-Introducís: mysql_secure_installation

sudo = super user do
apt = gestor de paquetes
install = quiero instalar un paquete
mysql-server = el paquete que quiero instalar

6.-Accedemos a MySQL con:
sudo mysql -u root -p

sudo = super user do
mysql = invocamos al gestor de bases de datos
-u = te paso el usuario
root = el nombre del usuario
-p = pideme la contraña