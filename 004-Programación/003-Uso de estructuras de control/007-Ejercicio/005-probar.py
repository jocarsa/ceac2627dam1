alumnos = []

while True:
    print("1.-Insertar registro")
    print("2.-Leer registro")

    opcion = input("Introduce tu opcion: ")

    try:
        if opcion == "1":
            print("Voy a insertar")
            alumno = input("Introduce un alumno: ")
            alumnos.append(alumno)

        elif opcion == "2":
            print("Voy a listar")
            print(alumnos)

    except Exception as e:
        print("No válido")