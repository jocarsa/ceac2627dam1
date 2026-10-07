class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.fecha_de_nacimiento = ""
    self.correo = ""
    self.telefono = ""
  def dimeNombre(self):
    print(self.nombre + " "+self.apellidos)
  def ponNombre(self,nuevonombre,nuevosapellidos):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos

# Esto es un paquete de datos
alumno1 = Alumno()
alumno1.nombre = "Heverton"
alumno1.apellidos = "Ferreira Maciel"
alumno1.dimeNombre()

# Y esto es otro paquete de datos
alumno2 = Alumno()
alumno2.nombre = "Adam"
alumno2.apellidos = "Founounou"
alumno2.dimeNombre()