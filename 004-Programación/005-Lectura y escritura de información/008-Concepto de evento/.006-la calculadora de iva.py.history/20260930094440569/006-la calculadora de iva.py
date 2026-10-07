# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

def calcula():
  print("Vamos a calcular")
  op1 = operando1.get()				# Dame  el contenido del entry 1
  op2 = operando2.get()				# Dame el contenido del entry 2
  suma = int(op1) + int(op2)						# Realiza una suma aritmética
  resultado.config(text=suma)	# Pon el resultado en el label ultimo

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Dime la base imponible")
etiqueta.pack(padx=10,pady=10)

base = tk.Entry()
base.pack(padx=10,pady=10)


boton = tk.Button(text="Vamos a calcular el IVA",command=calcula)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)
 
ventana.mainloop() # no te salgas, bucle infinito