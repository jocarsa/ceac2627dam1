class Animal:
    def __init__(self, micolor, miedad):
        self.color = micolor
        self.edad = miedad


class Mamifero(Animal):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def mama(self):
        return "Estoy mamando"


class Oviparo(Animal):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def mama(self):
        return "Estoy mamando"


class Gato(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def maulla(self):
        return "miau"


class Perro(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def ladra(self):
        return "guau"