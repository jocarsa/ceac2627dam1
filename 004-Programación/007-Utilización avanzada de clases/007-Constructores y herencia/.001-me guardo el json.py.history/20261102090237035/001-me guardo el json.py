import json

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

pedido1 = Pedido("2026-11-02","Jose Vicente","Carratala")
pedido1.productos.append(Producto("Producto1",34))
pedido1.productos.append(Producto("Producto2",45))

mijson = json.dumps(pedido1, default=lambda obj: obj.__dict__, indent=2, ensure_ascii=False)

print(mijson)
archivo = open("mipedido.json",'w')
