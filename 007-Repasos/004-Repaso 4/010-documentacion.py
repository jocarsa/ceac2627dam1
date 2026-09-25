"""
	Programa gestión de alumnos
  v0.1 por Jose Vicente Carratala
"""
# Primero el mensaje de bienvenida
print("Listado de alumnos v0.1")
print("En este programa guardas alumnos")
# Creo una lista de alumnos que estará vacía
alumnos = []
# Entro en un bucle infinito
while True:
  # Le enseño al usuario las opciones
  print("1.-Insertar un alumno")
  print("2.-Listado de alumnos")
  # Le pemito al usuario que coga una opción
  opcion = input("Escoge una opción: ")
  # Utilizo try y assert para salir del programa si la opción no es correcta
  try:
  	assert opcion == "1" or opcion == "2"
  except Exception:
    print("La opción que has cogido no es valida y me salgo")
    exit()
  if opcion == "1": # Si el usuario escoge la opción 1
    # Metemos un nuevo alumno
    print("Insertar un alumno")
    nuevoalumno = input("Dime el nombre del nuevo alumno: ")
    alumnos.append(nuevoalumno) # A una lista le añadimos nuevo elemento
  elif opcion == "2":	# Si el usuario escoge la opción 2
    print("Listado de alumnos:")
    print(alumnos)			# Imprimo directamente el listado de alumnos
    
