"""
	Listado de alumnos v0.1 por Jose Vicente Carratala
  Este programa crea un lista de alumnos
"""
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
        else:
            assert 4 < 3			# Introduzco una asercion para forzar un error

    except Exception as e:		# Capturo el error y lo saco por pantalla
        print("No válido")
        
        