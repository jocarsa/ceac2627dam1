# pip install ttkbootstrap
# pip3 install ttkbootstrap --break-system-packages

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# ============================================
# VENTANA
# ============================================

ventana = ttk.Window(
    title="Agenda de clientes",
    themename="flatly",
    size=(950, 580),
    resizable=(True, True)
)

ventana.place_window_center()


# ============================================
# FUNCIONES
# ============================================

def insertaCliente():
    stringnombre = inputnombre.get()
    stringapellidos = inputapellidos.get()
    stringemail = inputemail.get()

    # Evitar insertar registros completamente vacíos
    if stringnombre == "" and stringapellidos == "" and stringemail == "":
        estado.config(
            text="Introduce algún dato antes de guardar",
            bootstyle="danger"
        )
        return

    archivo = open("agenda.csv", "a")
    archivo.write(
        stringnombre + "," +
        stringapellidos + "," +
        stringemail + "\n"
    )
    archivo.close()

    # Limpiar formulario
    inputnombre.delete(0, tk.END)
    inputapellidos.delete(0, tk.END)
    inputemail.delete(0, tk.END)

    # Actualizar listado
    cargarClientes()

    estado.config(
        text="✓ Cliente guardado correctamente",
        bootstyle="success"
    )

    inputnombre.focus()


def cargarClientes():

    campodetexto.delete("1.0", tk.END)

    try:
        archivo = open("agenda.csv", "r")
        lineas = archivo.readlines()

        for linea in lineas:
            campodetexto.insert(tk.END, linea)

        archivo.close()

        contador.config(
            text=str(len(lineas)) + " clientes registrados"
        )

    except FileNotFoundError:
        contador.config(text="0 clientes registrados")


# ============================================
# CONTENEDOR PRINCIPAL
# ============================================

principal = ttk.Frame(
    ventana,
    padding=30
)

principal.pack(
    fill=BOTH,
    expand=True
)

principal.columnconfigure(0, weight=1)
principal.columnconfigure(1, weight=2)
principal.rowconfigure(1, weight=1)


# ============================================
# CABECERA
# ============================================

cabecera = ttk.Frame(principal)

cabecera.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky=EW,
    pady=(0, 25)
)

titulo = ttk.Label(
    cabecera,
    text="Agenda",
    font=("Arial", 26, "bold"),
    bootstyle="primary"
)

titulo.pack(anchor=W)

subtitulo = ttk.Label(
    cabecera,
    text="Gestión sencilla de clientes",
    font=("Arial", 11),
    bootstyle="secondary"
)

subtitulo.pack(anchor=W, pady=(3, 0))


# ============================================
# FORMULARIO IZQUIERDO
# ============================================

marco = ttk.Labelframe(
    principal,
    text=" Nuevo cliente ",
    padding=25,
    bootstyle="primary"
)

marco.grid(
    row=1,
    column=0,
    sticky=NSEW,
    padx=(0, 15)
)


# NOMBRE

nombre = ttk.Label(
    marco,
    text="Nombre",
    font=("Arial", 10, "bold")
)

nombre.pack(
    anchor=W,
    pady=(0, 5)
)

inputnombre = ttk.Entry(
    marco,
    font=("Arial", 11)
)

inputnombre.pack(
    fill=X,
    ipady=6,
    pady=(0, 20)
)


# APELLIDOS

apellidos = ttk.Label(
    marco,
    text="Apellidos",
    font=("Arial", 10, "bold")
)

apellidos.pack(
    anchor=W,
    pady=(0, 5)
)

inputapellidos = ttk.Entry(
    marco,
    font=("Arial", 11)
)

inputapellidos.pack(
    fill=X,
    ipady=6,
    pady=(0, 20)
)


# EMAIL

email = ttk.Label(
    marco,
    text="Correo electrónico",
    font=("Arial", 10, "bold")
)

email.pack(
    anchor=W,
    pady=(0, 5)
)

inputemail = ttk.Entry(
    marco,
    font=("Arial", 11)
)

inputemail.pack(
    fill=X,
    ipady=6,
    pady=(0, 25)
)


# BOTÓN

boton = ttk.Button(
    marco,
    text="＋  Insertar cliente",
    command=insertaCliente,
    bootstyle="primary"
)

boton.pack(
    fill=X,
    ipady=7
)


# MENSAJE DE ESTADO

estado = ttk.Label(
    marco,
    text="",
    font=("Arial", 9)
)

estado.pack(
    anchor=W,
    pady=(15, 0)
)


# ============================================
# PANEL DERECHO
# ============================================

derecha = ttk.Labelframe(
    principal,
    text=" Clientes ",
    padding=20,
    bootstyle="secondary"
)

derecha.grid(
    row=1,
    column=1,
    sticky=NSEW,
    padx=(15, 0)
)

derecha.columnconfigure(0, weight=1)
derecha.rowconfigure(1, weight=1)


# CONTADOR

contador = ttk.Label(
    derecha,
    text="0 clientes registrados",
    font=("Arial", 10),
    bootstyle="secondary"
)

contador.grid(
    row=0,
    column=0,
    sticky=W,
    pady=(0, 10)
)


# ============================================
# ÁREA DE TEXTO
# ============================================

marcotexto = ttk.Frame(derecha)

marcotexto.grid(
    row=1,
    column=0,
    sticky=NSEW
)

marcotexto.columnconfigure(0, weight=1)
marcotexto.rowconfigure(0, weight=1)


campodetexto = tk.Text(
    marcotexto,
    font=("Ubuntu Mono", 11),
    relief="flat",
    padx=15,
    pady=15,
    wrap="none"
)

campodetexto.grid(
    row=0,
    column=0,
    sticky=NSEW
)


# SCROLL

scroll = ttk.Scrollbar(
    marcotexto,
    orient=VERTICAL,
    command=campodetexto.yview
)

scroll.grid(
    row=0,
    column=1,
    sticky=NS
)

campodetexto.config(
    yscrollcommand=scroll.set
)


# ============================================
# PIE
# ============================================

pie = ttk.Label(
    principal,
    text="Agenda v0.2 · Python + Tkinter + ttkbootstrap",
    font=("Arial", 9),
    bootstyle="secondary"
)

pie.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky=W,
    pady=(20, 0)
)


# ============================================
# INICIO
# ============================================

cargarClientes()

inputnombre.focus()

ventana.mainloop()