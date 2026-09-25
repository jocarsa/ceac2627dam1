"""
  Programa gestión de alumnos
  v0.3 por Jose Vicente Carratala
"""

# Colores ANSI
RESET = "\033[0m"
AZUL = "\033[44m"
BLANCO = "\033[97m"
AMARILLO = "\033[93m"
VERDE = "\033[92m"
ROJO = "\033[91m"
CIAN = "\033[96m"

# Creo una lista de alumnos que estará vacía
alumnos = []

# Función para limpiar la pantalla
def limpiar():
  print("\033[2J\033[H",end="")

# Función para dibujar la cabecera
def cabecera():
  limpiar()
  print(AZUL + BLANCO)
  print("╔══════════════════════════════════════════════════════════════════════╗")
  print("║                                                                      ║")
  print("║                  SISTEMA DE GESTION DE ALUMNOS                       ║")
  print("║                            JOCARSA                                   ║")
  print("║                                                                      ║")
  print("╠══════════════════════════════════════════════════════════════════════╣")
  print("║  LISTADO DE ALUMNOS v0.3                              AÑO 2026       ║")
  print("╚══════════════════════════════════════════════════════════════════════╝")
  print(RESET)

# Entro en un bucle infinito
while True:

  cabecera()

  # Le enseño al usuario las opciones
  print(AZUL + BLANCO)
  print("╔══════════════════════════════════════════════════════════════════════╗")
  print("║                         MENU PRINCIPAL                               ║")
  print("╠══════════════════════════════════════════════════════════════════════╣")
  print("║                                                                      ║")
  print("║    " + AMARILLO + "[1]" + BLANCO + "  INSERTAR UN ALUMNO                                      ║")
  print("║                                                                      ║")
  print("║    " + AMARILLO + "[2]" + BLANCO + "  LISTADO DE ALUMNOS                                      ║")
  print("║                                                                      ║")
  print("║    " + AMARILLO + "[3]" + BLANCO + "  CALCULAR NOTA MEDIA                                     ║")
  print("║                                                                      ║")
  print("║    " + AMARILLO + "[4]" + BLANCO + "  SALIR                                                    ║")
  print("║                                                                      ║")
  print("╚══════════════════════════════════════════════════════════════════════╝")
  print(RESET)

  opcion = input(AZUL + VERDE + "C:\\ALUMNOS> Escoge una opción: " + RESET)

  if opcion == "1":

    cabecera()

    print(AZUL + BLANCO)
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║                       INSERTAR ALUMNO                                ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(RESET)

    nuevoalumno = input(AZUL + CIAN + "Nombre del alumno : " + RESET)
    nota = int(input(AZUL + CIAN + "Nota del alumno   : " + RESET))

    alumnos.append([nuevoalumno,nota])

    print()
    print(AZUL + VERDE + ">> ALUMNO INSERTADO CORRECTAMENTE <<" + RESET)

    input("\nPulsa ENTER para continuar...")

  elif opcion == "2":

    cabecera()

    print(AZUL + BLANCO)
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║                       LISTADO DE ALUMNOS                             ║")
    print("╠══════════════════════════════════════════════╦═══════════════════════╣")
    print("║ NOMBRE                                       ║ NOTA                  ║")
    print("╠══════════════════════════════════════════════╬═══════════════════════╣")

    for alumno in alumnos:
      nombre = alumno[0]
      nota = alumno[1]

      print("║",nombre.ljust(44),"║",str(nota).ljust(21),"║")

    print("╚══════════════════════════════════════════════╩═══════════════════════╝")
    print(RESET)

    input("\nPulsa ENTER para continuar...")

  elif opcion == "3":

    cabecera()

    print(AZUL + BLANCO)
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║                         NOTA MEDIA                                   ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(RESET)

    if len(alumnos) > 0:

      suma = 0

      for alumno in alumnos:
        suma = suma + alumno[1]

      media = suma / len(alumnos)

      print(AZUL + AMARILLO)
      print("Número de alumnos :",len(alumnos))
      print("Suma de notas     :",suma)
      print("Nota media        :",round(media,2))
      print(RESET)

    else:

      print(AZUL + ROJO)
      print("ERROR: NO HAY ALUMNOS INTRODUCIDOS")
      print(RESET)

    input("\nPulsa ENTER para continuar...")

  elif opcion == "4":

    cabecera()

    print(AZUL + AMARILLO)
    print()
    print("              ************************************")
    print("              *                                  *")
    print("              *    CERRANDO SISTEMA...           *")
    print("              *                                  *")
    print("              ************************************")
    print()
    print(RESET)

    break

  else:

    print(AZUL + ROJO)
    print("ERROR: OPCION NO RECONOCIDA")
    print(RESET)

    input("\nPulsa ENTER para continuar...")