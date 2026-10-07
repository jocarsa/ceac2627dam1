# Presentación
TITULO = "Calculadora de distancia recorrida"
VERSION = 0.2

print("╔══════════════════════════════════════════════╗")
print("║        CALCULADORA DE DISTANCIA              ║")
print("║                    v" + str(VERSION) + "                     ║")
print("╚══════════════════════════════════════════════╝")
print()

# El usuario introduce datos
print("┌──────────── DATOS DEL VIAJE ────────────────┐")

tiempo_en_carretera = input("│ Tiempo total del viaje (horas): ")
velocidad = input("│ Velocidad media (Km/h): ")
tiempo_descanso = input("│ Tiempo de descanso (horas): ")

print("└─────────────────────────────────────────────┘")

# Conversión de tipos
tiempo_en_carretera = float(tiempo_en_carretera)
velocidad = float(velocidad)
tiempo_descanso = float(tiempo_descanso)

# El programa hace cálculos
tiempo_conduciendo = tiempo_en_carretera - tiempo_descanso
distancia = tiempo_conduciendo * velocidad

# El programa ofrece resultados
print()
print("╔════════════════ RESULTADOS ═════════════════╗")
print("║")
print("║ Tiempo total:       ", tiempo_en_carretera, "h")
print("║ Tiempo de descanso: ", tiempo_descanso, "h")
print("║ Tiempo conduciendo: ", tiempo_conduciendo, "h")
print("║ Velocidad media:    ", velocidad, "Km/h")
print("║")
print("║ -------------------------------------------")
print("║ DISTANCIA RECORRIDA:", distancia, "Km")
print("║")
print("╚═════════════════════════════════════════════╝")