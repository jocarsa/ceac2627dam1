class Animal():
  def __init__(self):
		self.edad = 0
    self.color = ""
    self.nombre = ""
    
class Perro(Animal):
  def __init__(self):
    super()
  def ladra():
    return "guau"
    
class Gato(Animal):
  def __init__(self):
    super()
  def maulla():
    return "miau"