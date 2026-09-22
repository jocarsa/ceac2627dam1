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
    
class Perro():
  def __init__(self):
    self.nombre = ""
  def dimeNombre(self):
    print(self.nombre)

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

# Y ahora creo un perro
perro1 = Perro()
perro1.nombre = "Toby"
perro1.dimeNombre()


