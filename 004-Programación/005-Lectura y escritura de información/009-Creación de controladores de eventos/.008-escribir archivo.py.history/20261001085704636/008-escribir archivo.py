import tkinter as tk

ventana = tk.Tk()

titulo = tk.Label(text="Programa agenda v0.1")
titulo.pack(padx=20,pady=20)

nombre = tk.Label(ventana,text="Introduce el nombre del cliente")
nombre.pack(padx=20,pady=20)
inputnombre = tk.Entry(ventana)
inputnombre.pack(padx=20,pady=20)

ventana.mainloop()