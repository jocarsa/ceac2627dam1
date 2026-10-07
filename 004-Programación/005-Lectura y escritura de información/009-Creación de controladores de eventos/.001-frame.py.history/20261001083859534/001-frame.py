import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

etiqueta = tk.Label(marco,text="Hola mundo")
etiqueta.pack(padx=10,pady=10)

boton = tk.Button(marco,text="Pulsame")
boton.pack(padx=10,pady=10)

ventana.mainloop()