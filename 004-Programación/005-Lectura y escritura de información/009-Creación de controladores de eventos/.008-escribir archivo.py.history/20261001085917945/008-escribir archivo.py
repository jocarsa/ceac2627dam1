import tkinter as tk

ventana = tk.Tk()

titulo = tk.Label(ventana,text="Programa agenda v0.1")
titulo.pack(padx=20,pady=20)

nombre = tk.Label(ventana,text="Introduce el nombre del cliente")
nombre.pack(padx=20,pady=20)
inputnombre = tk.Entry(ventana)
inputnombre.pack(padx=20,pady=20)

apellidos = tk.Label(ventana,text="Introduce los apellidos del cliente")
apellidos.pack(padx=20,pady=20)
inputapellidos = tk.Entry(ventana)
inputapellidos.pack(padx=20,pady=20)

email = tk.Label(ventana,text="Introduce el email del cliente")
email.pack(padx=20,pady=20)
inputemail = tk.Entry(ventana)
inputemail.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx=20,pady=20)

ventana.mainloop()