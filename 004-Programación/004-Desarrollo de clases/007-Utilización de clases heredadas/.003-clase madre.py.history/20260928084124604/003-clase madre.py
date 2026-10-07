class Animal:
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.nombre = ""


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