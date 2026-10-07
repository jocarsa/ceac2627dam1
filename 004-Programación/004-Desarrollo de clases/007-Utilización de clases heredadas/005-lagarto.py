class Animal:
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.nombre = ""

    def mamar(self):
        return "El animal está mamando"


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