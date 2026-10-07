# Bienvenida
print("Aplicación Hospital v0.1")
print("por Jose Vicente Carratala")

# Defino lo que es un paciente
class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
# Creo una lista vacía de pacientes
lista_de_pacientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un paciente")
  print("2.-Listar los pacientes")
  opcion = input("Indica tu opción: ")
  if opcion == "1":
    print("Ahora vemos como insertamos un paciente")
  elif opcion == "2":
    print("Ahora listamos los pacientes·)