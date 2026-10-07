print("Listado de alumnos v0.1")
print("En este programa guardas alumnos")
alumnos = []
while True:
  print("1.-Insertar un alumno")
  print("2.-Listado de alumnos")
  opcion = input("Escoge una opción: ")
  try:
  	assert opcion == "1" or opcion == "2"
  except Exception:
    print("La opción que has cogido no es valida y me salgo")
    exit()
  if opcion == "1":
    print("Insertar un alumno")
    nuevoalumno = input("Dime el nombre del nuevo alumno: ")
    alumnos.append(nuevoalumno) # A una lista le añadimos nuevo elemento
  elif opcion == "2":
    print("Listado de alumnos:")
    print(alumnos)
    
