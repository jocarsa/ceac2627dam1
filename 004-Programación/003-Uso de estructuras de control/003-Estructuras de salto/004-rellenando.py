# Primero presento el programa
# CRUD = Create, Read, Update, Delete
"""
	Programa CRUD
  Versión 0.1
  por Jose Vicente Carratala
"""
# Mensaje de bienvenida
print("Programa CRUD v 0.1")
print("En este programa practicamos en clase")
# Entrar en un bucle infinito
while True:
  # Le enseño al usuario lo que puede hacer
	print("1.-Insertar un registro")
  print("2.-Leer los registros")
  print("3.-Actualizar un registro")
  print("4.-Eliminar un registro")
  # Le pregunto qué quiere hacer
	opcion = input("Escoge una de las opciones: ")
  # Anoto su decisión y tomo una acción - la acción puede ser
	if opcion == "1":
  	# 1.-Crear un nuevo registro
		print("Voy a crear un nuevo registro")
  elif opcion == "2":
   	# 2.-Listar los registros existentes
    print("Voy a listar los registros")
  elif opcion == "3":
  	# 3.-Actualizar un registro
    print("Voy a actualizar un registro")
  elif opcion == "4":
  	# 4.-Eliminar un registros
    print("Voy a eliminar un registro")
  else:
    print("opción no válida")