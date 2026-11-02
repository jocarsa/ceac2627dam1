# MongoDB que es la base de datos

sudo apt update
sudo apt install -y gnupg curl

curl -fsSL https://pgp.mongodb.com/server-8.0.asc | \
sudo gpg --dearmor -o /usr/share/keyrings/mongodb-server-8.0.gpg

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | \
sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list

sudo apt update
sudo apt install -y mongodb-org

# Instalar mongocompass - que es la interfaz:
https://www.mongodb.com/try/download/terraform-provider