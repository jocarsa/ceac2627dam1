print("Listado de alumnos v0.1")
print("En este programa guardas alumnos")
alumnos = []
while True:
  print("1.-Insertar un alumno")
  print("2.-Listado de alumnos")
  opcion = input("Escoge una opción: ")
  if opcion == "1":
    print("Insertar un alumno")
    nuevoalumno = input("Dime el nombre del nuevo alumno: ")
    alumnos.append(nuevoalumno)
  elif opcion == "2":
    print("Listado de alumnos:")
    print(alumnos)
    
