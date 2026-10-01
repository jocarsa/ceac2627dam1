import tkinter as tk

ventana = tk.Tk()
# Contenido del marco
marco = tk.Frame(ventana)
etiqueta = tk.Label(marco,text="Hola mundo")
etiqueta.pack(padx=10,pady=10)
boton = tk.Button(marco,text="Pulsame")
boton.pack(padx=10,pady=10)

# Botones de control
mostrar = tk.Button(ventana,text="Mostrar")
mostrar.pack(padx=10,pady=10)

ventana.mainloop()