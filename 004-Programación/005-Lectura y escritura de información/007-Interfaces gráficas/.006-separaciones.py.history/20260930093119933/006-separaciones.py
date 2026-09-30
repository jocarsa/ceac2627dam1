# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Hola mundo en Tkinter")
etiqueta.pack(padx=20,pady=20)

boton = tk.Button(text="Pulsame si te atreves")
boton.pack(padx=20,pady=20)

entrada = tk.Entry()
entrada.pack(padx=20,pady=20)
 
ventana.mainloop() # no te salgas, bucle infinito