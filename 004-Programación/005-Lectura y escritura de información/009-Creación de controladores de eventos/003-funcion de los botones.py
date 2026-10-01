import tkinter as tk

def muestraContenido():
  print("Te voy a mostrar el marco")

def ocultaContenido():
  print("Te voy a ocultar el marco")

ventana = tk.Tk()
# Contenido del marco
marco = tk.Frame(ventana)
etiqueta = tk.Label(marco,text="Hola mundo")
etiqueta.pack(padx=10,pady=10)
boton = tk.Button(marco,text="Pulsame")
boton.pack(padx=10,pady=10)

# Botones de control
mostrar = tk.Button(ventana,text="Mostrar",command=muestraContenido)
mostrar.pack(padx=10,pady=10)

ocultar = tk.Button(ventana,text="Ocultar",command=ocultaContenido)
ocultar.pack(padx=10,pady=10)

ventana.mainloop()