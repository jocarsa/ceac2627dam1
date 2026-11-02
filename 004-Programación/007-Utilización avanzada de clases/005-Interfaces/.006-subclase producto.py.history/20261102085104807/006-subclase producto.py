class Cliente():
  def __init__(self,minombre,misapellidos):
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():
  def __init__(self,minombre,miprecio):
    self.nombre = minombre
    self.precio = miprecio
    
class Pedido():
  def __init__(self,mifecha,minombre,misapellidos,miemail,mitelefono):
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos,miemail,mitelefono)
    self.productos = []
    

pedido1 = Pedido("2026-11-02","Jose Vicente","Carratala")
pedido1.productos.append("Producto1",34)
pedido1.productos.append("Producto2",45)

print(pedido1)