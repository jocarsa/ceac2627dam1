print("Programa en agenda v0.1")
print("por Jose Vicente Carratala")

while True:
  print("Escoge una opcion")
  print("1.-Insertar un registro")
  print("2.-Listado de registros")
  opcion = input("Indica tu opción: ")
  if opcion == "1":
  	nombre = input("Introduce un nombre: ")
    apellidos = input("Introduce unos apellidos: ")
    email = input("Introduce un email: ")
    archivo = open("agenda.csv",'a')
    archivo.write(nombre+","+apellidos+","+email+"\n")
    archivo.close()
	elif opcion == "2":
    archivo = open("agenda.csv",'r')