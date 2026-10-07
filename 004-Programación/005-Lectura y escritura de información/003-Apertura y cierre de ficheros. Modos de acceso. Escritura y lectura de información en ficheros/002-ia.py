import os
import time

# ============================================
# COLORES ANSI
# ============================================

RESET = "\033[0m"
NEGRITA = "\033[1m"

VERDE = "\033[92m"
AZUL = "\033[94m"
CYAN = "\033[96m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
GRIS = "\033[90m"
BLANCO = "\033[97m"

FONDO_AZUL = "\033[44m"


# ============================================
# FUNCIONES VISUALES
# ============================================

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def cabecera():
    print(CYAN + NEGRITA)
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                                                              ║")
    print("║                    ◉  JOCARSA AGENDA  ◉                     ║")
    print("║                                                              ║")
    print("║                  Sistema de contactos v0.1                   ║")
    print("║                por Jose Vicente Carratala                    ║")
    print("║                                                              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(RESET)


def pausa():
    input(GRIS + "\nPulsa ENTER para continuar..." + RESET)


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

while True:

    limpiar()
    cabecera()

    print(BLANCO + NEGRITA + "  MENÚ PRINCIPAL" + RESET)
    print(GRIS + "  ──────────────────────────────────────────────────────────" + RESET)

    print()
    print(CYAN + "  [ 1 ]" + RESET + "  ✚  Insertar un registro")
    print(CYAN + "  [ 2 ]" + RESET + "  ☰  Listado de registros")
    print(ROJO + "  [ 0 ]" + RESET + "  ✕  Salir")
    print()

    print(GRIS + "  ──────────────────────────────────────────────────────────" + RESET)

    opcion = input(
        AMARILLO + NEGRITA +
        "\n  ❯ Selecciona una opción: " +
        RESET
    )

    # ========================================
    # INSERTAR
    # ========================================

    if opcion == "1":

        limpiar()
        cabecera()

        print(VERDE + NEGRITA + "  ✚ NUEVO CONTACTO" + RESET)
        print(GRIS + "  ──────────────────────────────────────────────────────────" + RESET)
        print()

        nombre = input(CYAN + "  Nombre     │ " + RESET)
        apellidos = input(CYAN + "  Apellidos  │ " + RESET)
        email = input(CYAN + "  Email      │ " + RESET)

        archivo = open("agenda.csv", "a")
        archivo.write(nombre + "," + apellidos + "," + email + "\n")
        archivo.close()

        print()
        print(VERDE + "  ╔════════════════════════════════════════════╗")
        print("  ║  ✓ Contacto guardado correctamente        ║")
        print("  ╚════════════════════════════════════════════╝" + RESET)

        time.sleep(1)

        pausa()

    # ========================================
    # LISTAR
    # ========================================

    elif opcion == "2":

        limpiar()
        cabecera()

        print(AZUL + NEGRITA + "  ☰ LISTADO DE CONTACTOS" + RESET)
        print()

        try:
            archivo = open("agenda.csv", "r")
            lineas = archivo.readlines()
            archivo.close()

            print(
                CYAN + NEGRITA +
                "  ┌────────────────────┬──────────────────────────┬──────────────────────────────┐"
            )
            print(
                "  │ NOMBRE             │ APELLIDOS                │ EMAIL                        │"
            )
            print(
                "  ├────────────────────┼──────────────────────────┼──────────────────────────────┤"
                + RESET
            )

            for linea in lineas:

                datos = linea.strip().split(",")

                if len(datos) >= 3:
                    nombre = datos[0]
                    apellidos = datos[1]
                    email = datos[2]

                    print(
                        "  │ "
                        + f"{nombre:<18.18}"
                        + " │ "
                        + f"{apellidos:<24.24}"
                        + " │ "
                        + f"{email:<28.28}"
                        + " │"
                    )

            print(
                CYAN +
                "  └────────────────────┴──────────────────────────┴──────────────────────────────┘"
                + RESET
            )

            print(
                GRIS +
                "\n  Total de contactos: "
                + BLANCO + NEGRITA +
                str(len(lineas))
                + RESET
            )

        except FileNotFoundError:

            print(
                AMARILLO +
                "  ⚠ Todavía no existe ningún contacto en la agenda."
                + RESET
            )

        pausa()

    # ========================================
    # SALIR
    # ========================================

    elif opcion == "0":

        limpiar()

        print(CYAN + NEGRITA)
        print()
        print("        ╔══════════════════════════════════╗")
        print("        ║                                  ║")
        print("        ║        JOCARSA AGENDA            ║")
        print("        ║                                  ║")
        print("        ║       Hasta la próxima :)        ║")
        print("        ║                                  ║")
        print("        ╚══════════════════════════════════╝")
        print(RESET)

        break

    # ========================================
    # OPCIÓN INCORRECTA
    # ========================================

    else:

        print()
        print(
            ROJO + NEGRITA +
            "  ✕ Opción no válida. Introduce 0, 1 o 2."
            + RESET
        )

        time.sleep(1)