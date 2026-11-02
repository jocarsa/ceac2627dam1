
class Mamifero:
    def __init__(self, micolor, miedad):
        self.color = micolor
        self.edad = miedad

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


micifu = Gato("naranja", 0)
firulais = Perro("marrón", 3)

print(micifu.color)
print(micifu.edad)
print(micifu.maulla())
print(micifu.mama())

print(firulais.color)
print(firulais.edad)
print(firulais.ladra())
print(firulais.mama())
