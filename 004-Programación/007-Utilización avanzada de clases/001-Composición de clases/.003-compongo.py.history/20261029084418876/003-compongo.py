class Rueda():
  def __init__(self,mi_radio):
    radio = mi_radio
    
class Motor():
  def __init__(self,micilindrada,caballos):
    cilindrada = micilindrada
    potencia = caballos

class Coche():
  def __init__(self,combustible,ada,cv,micolor):
    tipocombustible = combustible
    sistema_ada = ada
    motor = Motor(45,100)
    rueda1 = Rueda(21)
    color = micolor
  def arrancar(self):
    return "El coche ha arrancado"
  def acelerar(self):
    return "El coche ha acelerado"
  
rueda = Rueda(21)
mimotor = Motor(45,100)

