class Mamifero():
  def __init__(self,micolor,miedad):
		color = micolor
    edad = miedad
    
class Gato(Mamifero):
  def __init__(self,micolor,miedad):
		super.__init__()

 	def maulla(self):
    return "miau"
    
class Perro(Mamifero):
  def __init__(self,micolor,miedad):
		super.__init__()

 	def ladra(self):
    return "guau"
    