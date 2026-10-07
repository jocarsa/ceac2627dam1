# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Hola mundo en Tkinter")
etiqueta.pack()

boton = tk.Button(text="Pulsame si te atreves")
boton.pack()

entrada = tk.Entry()
entrada.pack()
 
ventana.mainloop() # no te salgas, bucle infinito