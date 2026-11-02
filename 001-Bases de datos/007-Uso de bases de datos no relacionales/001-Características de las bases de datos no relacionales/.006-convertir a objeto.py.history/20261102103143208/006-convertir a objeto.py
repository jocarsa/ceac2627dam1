import json
from types import SimpleNamespace

archivocliente1 = open("mibasededatos/clientes/cliente1.json", 'r')

cliente = json.load(
    archivocliente1,
    object_hook=lambda datos: SimpleNamespace(**datos)
)

archivocliente1.close()

print(cliente)