# Bienvenida
print("Aplicación Hospital v0.1")
print("por Jose Vicente Carratala")


# Defino lo que es una persona
class Persona():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


# Defino lo que es un paciente
class Paciente(Persona):
    def __init__(self, nombre, apellidos, email):
        super().__init__(nombre, apellidos, email)


# Creo una lista vacía de pacientes
lista_de_pacientes = []


while True:
    print("Escoge una opción:")
    print("1.- Insertar un paciente")
    print("2.- Listar los pacientes")

    opcion = input("Indica tu opción: ")

    if opcion == "1":
        print("Ahora vemos cómo insertamos un paciente")

        # Le pido al usuario los datos del paciente
        nombre = input("Introduce el nombre del paciente: ")
        apellidos = input("Introduce los apellidos del paciente: ")
        email = input("Introduce el email del paciente: ")

        # Creo un paciente
        nuevo_paciente = Paciente(
            nombre,
            apellidos,
            email
        )

        # Añado el paciente a la lista
        lista_de_pacientes.append(nuevo_paciente)

    elif opcion == "2":
        print("Ahora listamos los pacientes")

        for paciente in lista_de_pacientes:
            print("-" * 30)
            print(paciente.nombre)
            print(paciente.apellidos)
            print(paciente.email)
            print("-" * 30)

    else:
        print("Opción no reconocida")