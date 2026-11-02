cat > instalar-mongodb9.sh <<'EOF'
#!/usr/bin/env bash
set -Eeuo pipefail

echo "========================================"
echo " INSTALADOR MONGODB 9 - UBUNTU 26.04"
echo "========================================"

# Cambiar a SI únicamente para instalación limpia
BORRAR_DATOS="NO"

# 1. Comprobar sistema
source /etc/os-release

if [[ "$ID" != "ubuntu" || "$VERSION_ID" != "26.04" ]]; then
    echo "ERROR: Este script requiere Ubuntu 26.04"
    exit 1
fi

ARCH=$(dpkg --print-architecture)
if [[ "$ARCH" != "amd64" && "$ARCH" != "arm64" ]]; then
    echo "Arquitectura no compatible: $ARCH"
    exit 1
fi

echo "Ubuntu: $VERSION_ID"
echo "Kernel: $(uname -r)"
echo "Arquitectura: $ARCH"

# 2. Comprobar datos existentes
if [[ "$BORRAR_DATOS" != "SI" ]]; then
    if [[ -d /var/lib/mongodb ]] &&
       [[ -n "$(sudo ls -A /var/lib/mongodb)" ]]; then
        echo
        echo "ATENCION: Existen datos de MongoDB."
        echo "No se puede garantizar que MongoDB 9"
        echo "abra directamente datos de versiones anteriores."
        echo "Realiza backup y migración antes de continuar."
        exit 1
    fi
else
    echo
    echo "ATENCION: SE BORRARAN LOS DATOS EXISTENTES"
    read -r -p "Escribe BORRAR para confirmar: " CONFIRMAR
    [[ "$CONFIRMAR" == "BORRAR" ]] || exit 1
fi

# 3. Detener servicios anteriores
echo "Deteniendo servicios anteriores..."

sudo systemctl stop mongod 2>/dev/null || true
sudo systemctl stop mongodb 2>/dev/null || true
sudo systemctl disable mongod 2>/dev/null || true

# 4. Eliminar paquetes anteriores
echo "Desinstalando MongoDB anterior..."

mapfile -t PAQUETES < <(
    dpkg-query -W -f='${binary:Package}\n' 2>/dev/null |
    grep -E '^(mongodb-org|mongodb-enterprise|mongodb-server|mongodb-clients|mongodb-mongosh|mongodb-database-tools|mongodb$)' || true
)

if (( ${#PAQUETES[@]} > 0 )); then
    sudo apt-get purge -y "${PAQUETES[@]}"
fi

# 5. Eliminar repositorios anteriores
echo "Limpiando repositorios..."

sudo rm -f /etc/apt/sources.list.d/mongodb-org-*.list
sudo rm -f /etc/apt/sources.list.d/mongodb-enterprise-*.list

# 6. Borrar datos solo si se solicita
if [[ "$BORRAR_DATOS" == "SI" ]]; then
    sudo rm -rf /var/lib/mongodb
    sudo rm -rf /var/log/mongodb
fi

# 7. Instalar dependencias
echo "Instalando dependencias..."

sudo apt-get update
sudo apt-get install -y curl gnupg ca-certificates

# 8. Importar clave oficial
echo "Importando clave MongoDB 9..."

curl -fsSL https://pgp.mongodb.com/server-9.asc |
    gpg --dearmor |
    sudo tee /usr/share/keyrings/mongodb-server-9.gpg > /dev/null

# 9. Configurar repositorio Ubuntu 26.04
echo "Configurando repositorio..."

echo "deb [ arch=$ARCH signed-by=/usr/share/keyrings/mongodb-server-9.gpg ] https://repo.mongodb.org/apt/ubuntu resolute/mongodb-org/9.0 multiverse" |
    sudo tee /etc/apt/sources.list.d/mongodb-org-9.0.list

# 10. Instalar MongoDB 9
echo "Instalando MongoDB..."

sudo apt-get update
sudo apt-get install -y mongodb-org

# 11. Activar servicio
echo "Iniciando MongoDB..."

sudo systemctl daemon-reload
sudo systemctl enable --now mongod

# 12. Comprobar instalación
echo
echo "========================================"
echo " VERIFICACION"
echo "========================================"

mongod --version | head -n 3

if sudo systemctl is-active --quiet mongod; then
    echo "Servicio MongoDB: ACTIVO"
else
    echo "ERROR: MongoDB no ha arrancado"
    sudo journalctl -u mongod -n 40 --no-pager
    exit 1
fi

echo
echo "Probando conexión..."

mongosh --quiet --eval \
'printjson(db.adminCommand({ping:1}))'

echo
echo "========================================"
echo " INSTALACION FINALIZADA"
echo "========================================"
EOF

chmod +x instalar-mongodb9.sh
./instalar-mongodb9.sh