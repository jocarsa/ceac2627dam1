
class Mamifero:
    def __init__(self, micolor, miedad):
        self.color = micolor
        self.edad = miedad


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

print(micifu.color)
print(micifu.edad)
print(micifu.maulla())
