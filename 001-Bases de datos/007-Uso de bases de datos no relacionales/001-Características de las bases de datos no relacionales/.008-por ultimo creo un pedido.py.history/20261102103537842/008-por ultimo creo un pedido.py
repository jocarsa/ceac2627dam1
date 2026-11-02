import json
# Creo una clase Cliente vacia
class Cliente:
    pass
# Creo una clase Producto vacía
class Producto:
    pass
# Creo una clase Pedido de verdad
class Pedido():
  def __init__(self):
# Cargo los objetos del disco duro
archivocliente1 = open("mibasededatos/clientes/cliente1.json", 'r')
archivoproducto1 = open("mibasededatos/productos/producto1.json", 'r')
# Los convierto de JSON a objetos
cliente = json.load(
    archivocliente1,
    object_hook=lambda datos: type("Cliente", (), datos)()
)
producto = json.load(
    archivoproducto1,
    object_hook=lambda datos: type("Producto", (), datos)()
)
# Cierro
archivocliente1.close()

print(cliente)
