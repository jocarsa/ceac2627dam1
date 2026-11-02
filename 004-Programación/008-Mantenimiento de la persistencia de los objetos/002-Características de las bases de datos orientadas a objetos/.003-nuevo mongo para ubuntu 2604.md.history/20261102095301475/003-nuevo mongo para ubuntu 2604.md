sudo apt update
sudo apt install -y curl gnupg

curl -fsSL https://pgp.mongodb.com/server-9.0.asc | \
sudo gpg --dearmor -o /usr/share/keyrings/mongodb-server-9.0.gpg

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-9.0.gpg ] https://repo.mongodb.org/apt/ubuntu resolute/mongodb-org/9.0 multiverse" | \
sudo tee /etc/apt/sources.list.d/mongodb-org-9.0.list

sudo apt update
sudo apt install -y mongodb-org

sudo systemctl enable --now mongod