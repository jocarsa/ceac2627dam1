print("Listado de alumnos v0.1")
print("En este programa guardas alumnos")
alumnos = []
while True:
  opcion = input("Escoge una opción: ")

  if opcion == "1":
    print("Insertar un alumno")
    nuevoalumno = input("Dime el nombre del nuevo alumno: ")
    alumnos.append(nuevoalumno)
  elif opcion == "2":
    print("Listame los alumnos")
