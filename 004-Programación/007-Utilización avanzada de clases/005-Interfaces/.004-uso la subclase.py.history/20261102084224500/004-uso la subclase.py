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
    
cliente1 = Cliente("Jose Vicente","Carratala","info@jocarsa.com","620891718")