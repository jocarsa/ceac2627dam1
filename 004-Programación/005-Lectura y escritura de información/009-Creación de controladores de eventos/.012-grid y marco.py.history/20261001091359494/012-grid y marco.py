import tkinter as tk

ventana = tk.Tk()

def insertaCliente():
  print("Voy a insertar un cliente")
  stringnombre = inputnombre.get()
  stringapellidos = inputapellidos.get()
  stringemail = inputemail.get()
  archivo = open("agenda.csv",'a')
  archivo.write(stringnombre+","+stringapellidos+","+stringemail+"\n")
  archivo.close()
  campodetexto.delete("1.0", tk.END)	# Primero borra todo lo que haya
  archivo = open("agenda.csv",'r')
  lineas = archivo.readlines()
  for linea in lineas:
    campodetexto.insert(tk.END, linea)	# Insertame una linea
  archivo.close()

marco = tk.Frame(ventana)

titulo = tk.Label(marco,text="Programa agenda v0.1")
titulo.pack(padx=20,pady=20)

nombre = tk.Label(marco,text="Introduce el nombre del cliente")
nombre.pack(padx=2,pady=2)
inputnombre = tk.Entry(marco)
inputnombre.pack(padx=20,pady=20)

apellidos = tk.Label(marco,text="Introduce los apellidos del cliente")
apellidos.pack(padx=2,pady=2)
inputapellidos = tk.Entry(marco)
inputapellidos.pack(padx=20,pady=20)

email = tk.Label(marco,text="Introduce el email del cliente")
email.pack(padx=2,pady=2)
inputemail = tk.Entry(marco)
inputemail.pack(padx=20,pady=20)

boton = tk.Button(marco,text="Insertar cliente",command=insertaCliente)
boton.pack(padx=20,pady=20)

marco.grid(row=0,column=0)

campodetexto = tk.Text(ventana)
campodetexto.grid(row=0,column=1,padx=20,pady=20)

ventana.mainloop()