import json

class Cliente:
    pass
class Producto:
    pass

archivocliente1 = open("mibasededatos/clientes/cliente1.json", 'r')
archivoproducto1 = open("mibasededatos/productos/producto1.json", 'r')

cliente = json.load(
    archivocliente1,
    object_hook=lambda datos: type("Cliente", (), datos)()
)

archivocliente1.close()

print(cliente)
