print("Programa agenda JSON v0.1")
agenda = []
while True:
  print("Escoge una opcion:")
  print("1.-Insertar un registro")
  print("2.-Listar registros")
  opcion = input("Tu opción: ")
  if opcion == "1":
    nombre = input("Introduce el nombre de la persona: ")
    apellidos = input("Introduce los apellidos de la persona: ")
    email = input("Introduce el email de la persona: ")
    # A la lista le añadimos un diccionario
    agenda.append({"nombre":nombre,"apellidos":apellidos,"email":email})
  elif opcion == "2":
    print(agenda)