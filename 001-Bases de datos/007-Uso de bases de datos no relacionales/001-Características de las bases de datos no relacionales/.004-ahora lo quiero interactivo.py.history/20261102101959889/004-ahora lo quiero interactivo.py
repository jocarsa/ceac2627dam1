import json
import os
from datetime import datetime

class Cliente():
  def __init__(self,minombre,misapellidos):
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():
  def __init__(self,minombre,miprecio):
    self.nombre = minombre
    self.precio = miprecio

class Pedido():
  def __init__(self,mifecha,minombre,misapellidos):
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []

fecha = input("Introduce la fecha del pedido: ")
pedido1 = Pedido("2026-11-02","Jose Vicente","Carratala")
pedido1.productos.append(Producto("Producto1",34))
pedido1.productos.append(Producto("Producto2",45))

mijson = json.dumps(pedido1, default=lambda obj: obj.__dict__, indent=2, ensure_ascii=False)

# Crear carpeta json si no existe
os.makedirs("json", exist_ok=True)

# Generar nombre con timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
archivo = f"json/{timestamp}.json"

# Guardar archivo
with open(archivo, "w", encoding="utf-8") as f:
    f.write(mijson)

print(mijson)
print("Archivo guardado en:", archivo)
