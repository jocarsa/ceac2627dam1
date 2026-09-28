class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

lista_de_pacientes = []
lista_de_pacientes.append(Paciente("Juan","Lopez","juan@lopez.com"))
lista_de_pacientes.append(Paciente("Maria","Garcia","maria@garcia.com"))

print(lista_de_pacientes)