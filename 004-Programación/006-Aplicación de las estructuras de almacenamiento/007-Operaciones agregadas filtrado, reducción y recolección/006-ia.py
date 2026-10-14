
import json
import os

archivo = "agenda.json"
agenda = []

print("╔══════════════════════════════════════╗")
print("║         AGENDA JSON v0.2             ║")
print("╚══════════════════════════════════════╝")

while True:
    print("\n" + "═" * 42)
    print("           MENÚ PRINCIPAL")
    print("═" * 42)
    print("  1. Añadir contacto")
    print("  2. Listar contactos")
    print("  3. Guardar agenda en JSON")
    print("  4. Cargar agenda desde JSON")
    print("  5. Salir")
    print("═" * 42)

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("\n--- NUEVO CONTACTO ---")

        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        email = input("Email: ").strip()

        contacto = {
            "nombre": nombre,
            "apellidos": apellidos,
            "email": email
        }

        agenda.append(contacto)
        print("\n✓ Contacto añadido correctamente.")

    elif opcion == "2":
        print("\n--- LISTADO DE CONTACTOS ---")

        if len(agenda) == 0:
            print("La agenda está vacía.")
        else:
            print(f"Total de contactos: {len(agenda)}\n")

            for indice, contacto in enumerate(agenda, start=1):
                print("─" * 42)
                print(f"Contacto #{indice}")
                print(f"  Nombre:    {contacto['nombre']}")
                print(f"  Apellidos: {contacto['apellidos']}")
                print(f"  Email:     {contacto['email']}")

            print("─" * 42)

    elif opcion == "3":
        print("\n--- GUARDAR AGENDA ---")

        try:
            with open(archivo, "w", encoding="utf-8") as fichero:
                json.dump(agenda, fichero, indent=4, ensure_ascii=False)

            print(f"✓ Agenda guardada en '{archivo}'.")
            print(f"✓ {len(agenda)} contactos guardados.")

        except OSError as error:
            print(f"✗ Error al guardar: {error}")

    elif opcion == "4":
        print("\n--- CARGAR AGENDA ---")

        if os.path.exists(archivo):
            try:
                with open(archivo, "r", encoding="utf-8") as fichero:
                    datos = json.load(fichero)

                if isinstance(datos, list):
                    agenda = datos
                    print("✓ Agenda cargada correctamente.")
                    print(f"✓ {len(agenda)} contactos encontrados.")
                else:
                    print("✗ El archivo no contiene una lista.")

            except (OSError, json.JSONDecodeError) as error:
                print(f"✗ Error al cargar: {error}")
        else:
            print("✗ Todavía no existe el archivo agenda.json.")

    elif opcion == "5":
        print("\nGracias por utilizar Agenda JSON.")
        print("¡Hasta pronto!")
        break

    else:
        print("\n✗ Opción incorrecta. Inténtalo de nuevo.")
