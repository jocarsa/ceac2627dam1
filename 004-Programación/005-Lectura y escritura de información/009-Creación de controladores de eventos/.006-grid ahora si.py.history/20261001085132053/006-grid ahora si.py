import tkinter as tk

ventana = tk.Tk()

texto1 = tk.Label(text="Soy el texto 1")
texto1.grid(row=0,column=0,padx=10,pady=10)

texto2 = tk.Label(text="Soy el texto 2")
texto2.grid(row=0,column=1)

texto3 = tk.Label(text="Soy el texto 3")
texto3.grid(row=1,column=0)

texto4 = tk.Label(text="Soy el texto 4")
texto4.grid(row=1,column=1)

ventana.mainloop()