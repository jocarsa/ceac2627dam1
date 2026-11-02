import json

class Cliente:
    pass

archivocliente1 = open("mibasededatos/clientes/cliente1.json", 'r')

cliente = json.load(
    archivocliente1,
    object_hook=lambda datos: type("Objeto", (), datos)()
)

archivocliente1.close()

print(cliente)
