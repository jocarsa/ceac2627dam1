# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

def calcula():
  print("Vamos a calcular")
  op1 = operando1.get()
  op2 = operando2.get()

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack(padx=10,pady=10)

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Vamos a calcular",command=calcula)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)
 
ventana.mainloop() # no te salgas, bucle infinito