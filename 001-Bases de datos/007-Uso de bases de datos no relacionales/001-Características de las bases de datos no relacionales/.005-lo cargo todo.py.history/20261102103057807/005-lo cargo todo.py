import json
archivocliente1 = open("mibasededatos/clientes/cliente1.json",'r')
cliente = json.load(archivocliente1)

print(cliente)