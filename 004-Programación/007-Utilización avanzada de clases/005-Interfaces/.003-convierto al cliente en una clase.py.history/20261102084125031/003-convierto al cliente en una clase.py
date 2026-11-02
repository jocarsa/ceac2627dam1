class Cliente():
  def __init__(self,minombre,misapellidos,miemail,mitelefono):
    self.nombre = minombre
    self.apellidos = misapellidos
    self.email = miemail
    self.telefono = mitelefono

class Pedido():
  def __init__(self,mifecha,micliente):
    self.fecha = mifecha
    self.cliente = Cliente()
    
pedido1 = Pedido("2026-11-02","Jose Vicente")
print(pedido1)
pedido2 = Pedido("2026-11-03","Juan")
print(pedido2)