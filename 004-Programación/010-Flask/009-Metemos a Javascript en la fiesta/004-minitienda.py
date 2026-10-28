# Flask permite crear webs
# render_template permite llamar a html
# request permite enviar información en formularios
from flask import Flask,render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("tienda.html")

@aplicacion.route("/datos")
def datos():
  return """
  	
[
  {"nombre":"Zapatillas running","descripcion":"Zapatillas ligeras para correr","precio":"59"},
  {"nombre":"Zapatillas fútbol","descripcion":"Botas de fútbol para césped artificial","precio":"75"},
  {"nombre":"Zapatillas baloncesto","descripcion":"Zapatillas de baloncesto con amortiguación","precio":"89"},
  {"nombre":"Camiseta deportiva","descripcion":"Camiseta transpirable de entrenamiento","precio":"19"},
  {"nombre":"Pantalón corto","descripcion":"Pantalón corto para actividades deportivas","precio":"24"},
  {"nombre":"Sudadera deportiva","descripcion":"Sudadera con capucha para entrenamiento","precio":"45"},
  {"nombre":"Chándal completo","descripcion":"Conjunto deportivo de chaqueta y pantalón","precio":"69"},
  {"nombre":"Calcetines deportivos","descripcion":"Pack de tres pares de calcetines","precio":"12"},
  {"nombre":"Mochila deportiva","descripcion":"Mochila de entrenamiento de 30 litros","precio":"39"},
  {"nombre":"Bolsa de gimnasio","descripcion":"Bolsa deportiva con compartimento para calzado","precio":"35"},
  {"nombre":"Balón de fútbol","descripcion":"Balón de fútbol tamaño 5","precio":"29"},
  {"nombre":"Balón de baloncesto","descripcion":"Balón de baloncesto de competición","precio":"32"},
  {"nombre":"Balón de voleibol","descripcion":"Balón de voleibol para interior","precio":"27"},
  {"nombre":"Raqueta de tenis","descripcion":"Raqueta de tenis de grafito","precio":"95"},
  {"nombre":"Pala de pádel","descripcion":"Pala de pádel de fibra de carbono","precio":"110"},
  {"nombre":"Pelotas de tenis","descripcion":"Bote de tres pelotas de tenis","precio":"8"},
  {"nombre":"Guantes de portero","descripcion":"Guantes de fútbol con agarre reforzado","precio":"42"},
  {"nombre":"Espinilleras","descripcion":"Protecciones ligeras para fútbol","precio":"15"},
  {"nombre":"Comba deportiva","descripcion":"Cuerda de saltar ajustable","precio":"14"},
  {"nombre":"Mancuernas 5 kg","descripcion":"Pareja de mancuernas de cinco kilogramos","precio":"39"},
  {"nombre":"Mancuernas 10 kg","descripcion":"Pareja de mancuernas de diez kilogramos","precio":"69"},
  {"nombre":"Esterilla fitness","descripcion":"Esterilla antideslizante para ejercicios","precio":"22"},
  {"nombre":"Bandas elásticas","descripcion":"Juego de bandas de resistencia","precio":"18"},
  {"nombre":"Banco de musculación","descripcion":"Banco ajustable para entrenamiento de fuerza","precio":"149"},
  {"nombre":"Bicicleta estática","descripcion":"Bicicleta de ejercicio con pantalla digital","precio":"249"},
  {"nombre":"Casco de ciclismo","descripcion":"Casco ligero con ventilación","precio":"49"},
  {"nombre":"Gafas de natación","descripcion":"Gafas de piscina antivaho","precio":"16"},
  {"nombre":"Gorro de natación","descripcion":"Gorro de silicona para piscina","precio":"9"},
  {"nombre":"Botella deportiva","descripcion":"Botella reutilizable de un litro","precio":"13"},
  {"nombre":"Reloj deportivo","descripcion":"Reloj con pulsómetro y seguimiento de actividad","precio":"129"}
]

  """

if __name__ == "__main__":
  aplicacion.run()