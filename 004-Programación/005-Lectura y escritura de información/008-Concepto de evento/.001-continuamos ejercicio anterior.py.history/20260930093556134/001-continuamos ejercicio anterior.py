# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack(padx=20,pady=20)

operando1 = tk.Entry()
operando1.pack(padx=20,pady=20)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack(padx=20,pady=20)

operando2 = tk.Entry()
operando2.pack(padx=20,pady=20)

boton = tk.Button(text="Vamos a calcular")
boton.pack(padx=20,pady=20)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=20,pady=20)
 
ventana.mainloop() # no te salgas, bucle infinito