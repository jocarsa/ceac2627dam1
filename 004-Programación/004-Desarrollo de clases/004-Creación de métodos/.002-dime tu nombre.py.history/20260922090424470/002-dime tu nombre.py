class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.fecha_de_nacimiento = ""
    self.correo = ""
    self.telefono = ""
  def dimeNombre():
    print(self.nombre + " "+self.apellidos)
  def ponNombre(nuevonombre,nuevosapellidos):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos
    
alumno1 = Alumno()
alumno1.nombre = "Heverton"
alumno1.apellidos = "Ferreira Maciel"

alumno2 = Alumno()
alumno2.nombre = "Adam"
alumno2.apellidos = "Founounou"