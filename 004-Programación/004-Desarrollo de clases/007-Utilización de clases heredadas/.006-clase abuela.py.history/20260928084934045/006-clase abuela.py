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


class Oviparo(Animal):
    def __init__(self):
        super().__init__()

    def reptar(self):
        return "Estoy reptando"


class Perro(Viviparo):
    def __init__(self):
        super().__init__()

    def ladra(self):
        return "guau"


class Gato(Viviparo):
    def __init__(self):
        super().__init__()

    def maulla(self):
        return "miau"


class Lagarto(Oviparo):
    def __init__(self):
        super().__init__()


mike = Lagarto()

print(mike.mamar())