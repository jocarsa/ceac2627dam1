# imprimir un mensaje de bienvenida
print("agenda v0.1")
print("por Jose Vicente Carratala")

#Entro en un bucle infinito
while True:
  print("Escoge una opcion:")
  
  # introducir datos
  nombre = input("Dime un nombre: ")
  apellidos = input("Dime unos apellidos: ")
  email = input("Dime un email: ")

  # guardar los datos a un archivo
  archivo = open("agenda.csv",'a')
  archivo.write(nombre+","+apellidos+","+email+"\n")
  archivo.close()
