class Animal:
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.nombre = ""
    
      
class Viviparo(Animal):
  	def __init__(self):
      	super().__init__()
    def mamar(self):
        return "El animal está mamando"
      
class Oviparo(Animal)
		def __init__(self):
				super().__init__()
    def reptar(self):
      	return "estoy reptando"

class Perro(Animal):
    def __init__(self):
        super().__init__()

    def ladra(self):
        return "guau"


class Gato(Animal):
    def __init__(self):
        super().__init__()

    def maulla(self):
        return "miau"


class Lagarto(Animal):
    def __init__(self):
        super().__init__()


mike = Lagarto()
print(mike.mamar())