archivo = open("Publicado - Aprende programación con Python.md",'r')

documento = ""
lineas = archivo.readlines()
for linea in lineas:
  print(linea)
  
archivo.close()