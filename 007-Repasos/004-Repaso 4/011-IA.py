"""
  Programa gestión de alumnos
  v0.2 por Jose Vicente Carratala
"""

# Primero el mensaje de bienvenida
print("Listado de alumnos v0.2")
print("En este programa guardas alumnos y sus notas")

# Creo una lista de alumnos que estará vacía
alumnos = []

# Entro en un bucle infinito
while True:
  # Le enseño al usuario las opciones
  print("1.-Insertar un alumno")
  print("2.-Listado de alumnos")
  print("3.-Nota media de los alumnos")

  # Le permito al usuario que coja una opción
  opcion = input("Escoge una opción: ")

  # Utilizo try y assert para salir del programa si la opción no es correcta
  try:
    assert opcion == "1" or opcion == "2" or opcion == "3"
  except Exception:
    print("La opción que has cogido no es válida y me salgo")
    exit()

  if opcion == "1":
    # Metemos un nuevo alumno
    print("Insertar un alumno")
    nuevoalumno = input("Dime el nombre del nuevo alumno: ")
    nota = int(input("Dime la nota del alumno: "))

    # Guardamos nombre y nota
    alumnos.append([nuevoalumno,nota])

  elif opcion == "2":
    # Mostramos los alumnos
    print("Listado de alumnos:")

    for alumno in alumnos:
      print("Nombre:",alumno[0],"Nota:",alumno[1])

  elif opcion == "3":
    # Calculamos la nota media
    suma = 0

    for alumno in alumnos:
      suma = suma + alumno[1]

    media = suma / len(alumnos)

    print("La nota media de los alumnos es:",media)