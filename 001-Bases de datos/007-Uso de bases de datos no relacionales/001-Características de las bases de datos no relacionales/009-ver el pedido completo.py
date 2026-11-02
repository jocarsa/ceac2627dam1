
import json

# Creo una clase Cliente vacía
class Cliente:
    pass

# Creo una clase Producto vacía
class Producto:
    pass

# Creo una clase Pedido de verdad
class Pedido:
    def __init__(self, mifecha):
        self.fecha = mifecha
        self.cliente = ""
        self.producto = ""

# Función para convertir diccionarios en objetos
def convertir_a_objeto(datos, clase):
    objeto = clase()
    objeto.__dict__.update(datos)
    return objeto

# Cargo los objetos del disco duro
archivocliente1 = open("mibasededatos/clientes/cliente1.json", "r")
archivoproducto1 = open("mibasededatos/productos/producto1.json", "r")

# Los convierto de JSON a objetos
cliente = convertir_a_objeto(json.load(archivocliente1), Cliente)
producto = convertir_a_objeto(json.load(archivoproducto1), Producto)

# Cierro los archivos
archivocliente1.close()
archivoproducto1.close()

# Creo el pedido
pedido1 = Pedido("2026-11-02")
pedido1.cliente = cliente
pedido1.producto = producto

# Muestro el pedido completo
print(json.dumps(
    pedido1,
    default=lambda obj: obj.__dict__,
    indent=2,
    ensure_ascii=False
))
