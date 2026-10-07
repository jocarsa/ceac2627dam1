""" 
Lista de la compra v0.1
"""

print("Programa lista de la compra")
lista_de_la_compra = []

while True:
  print("Escoge una opcion")
  print("1.-Insertar un nuevo elemento")
  print("2.-Listar elementos")
  if opcion == "1":
  	elemento = input("Introduce un nuevo elemento")
    lista_de_la_compra.append(elemento)
	elif opcion == "2":
    print(lista_de_la_compra)