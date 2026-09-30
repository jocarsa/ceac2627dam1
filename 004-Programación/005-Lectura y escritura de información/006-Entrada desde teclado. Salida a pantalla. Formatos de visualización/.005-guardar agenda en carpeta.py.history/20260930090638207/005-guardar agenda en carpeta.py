import os

# imprimir un mensaje de bienvenida
print("agenda v0.1")
print("por Jose Vicente Carratala")

os.mkdir("mibasededatos")

#Entro en un bucle infinito
while True:
  print("Escoge una opcion:")
  print("1.-insertar datos")
  print("2.-leer datos")
  print("3.-salir del programa")
  opcion = input("Escoge una opción: ")
  if opcion == "1":
    # introducir datos
    nombre = input("Dime un nombre: ")
    apellidos = input("Dime unos apellidos: ")
    email = input("Dime un email: ")

    # guardar los datos a un archivo
    archivo = open("agenda.csv",'a')
    archivo.write(nombre+","+apellidos+","+email+"\n")
    archivo.close()
  elif opcion == "2":
    archivo = open("agenda.csv",'r')
    lineas = archivo.readlines()
    for linea in lineas:
      print(linea)
    archivo.close()
  elif opcion == "3":
    exit()
