from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

# Función para agregar un usuario
def agregar_usuario():
    # Obtener datos de las entradas
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    especialidad = entrada_especialidad.get()
    presente = entrada_presente.get()
    ausente = entrada_ausente.get()

    # Verificar si los campos no están vacíos
    if nombre and edad and especialidad and presente and ausente:
        # Agregar usuario a la tabla
        tabla1.insert("", END, text=nombre, values=(edad, especialidad, presente, ausente))

        # Limpiar las entradas
        entrada_nombre.delete(0, tk.END)
        entrada_edad.delete(0, tk.END)
        entrada_especialidad.delete(0, tk.END)
        entrada_presente.delete(0, tk.END)
        entrada_ausente.delete(0, tk.END)

        # Cerrar la ventana de agregar usuario
        ventana_agregar.destroy()

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", f"Docente {nombre} agregado exitosamente")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")

# Función para mostrar la ventana de agregar usuario
def mostrar_ventana_agregar():
    global ventana_agregar, entrada_nombre, entrada_edad, entrada_especialidad, entrada_presente, entrada_ausente
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Docente")
    ventana_agregar.geometry("400x400")  # Ajuste del tamaño
    ventana_agregar.configure(bg="lightblue")

    # Etiquetas y entradas
    ttk.Label(ventana_agregar, text="Nombre:").pack(pady=5)
    entrada_nombre = ttk.Entry(ventana_agregar)
    entrada_nombre.pack(pady=5)

    ttk.Label(ventana_agregar, text="Edad:").pack(pady=5)
    entrada_edad = ttk.Entry(ventana_agregar)
    entrada_edad.pack(pady=5)

    ttk.Label(ventana_agregar, text="Especialidad:").pack(pady=5)
    entrada_especialidad = ttk.Entry(ventana_agregar)
    entrada_especialidad.pack(pady=5)

    ttk.Label(ventana_agregar, text="Presente:").pack(pady=5)
    entrada_presente = ttk.Entry(ventana_agregar)
    entrada_presente.pack(pady=5)

    ttk.Label(ventana_agregar, text="Ausente:").pack(pady=5)
    entrada_ausente = ttk.Entry(ventana_agregar)
    entrada_ausente.pack(pady=5)

    # Botón para agregar usuario
    ttk.Button(ventana_agregar, text="Agregar", command=agregar_usuario).pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menu principal - DocWar 1.0")
ventana.geometry("900x500")
ventana.configure(bg="lightblue")

# Botones
add_button = ttk.Button(ventana, text="Agregar Docente", style='TButton', command=mostrar_ventana_agregar)
add_button.place(x=200, y=350)

edit_button = ttk.Button(ventana, text="Editar Información", style='TButton', command=lambda: print("Editar Información"))
edit_button.place(x=690, y=350)

# Boton docente
docente_button = ttk.Button(ventana, text="    Entrar    ", style='TButton', command=lambda: print("Entrar"))
docente_button.place(x=690, y=420)

# Tabla de información sobre los funcionarios
tabla1 = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4"))
tabla1.column("#0", width=150)
tabla1.column("col1", width=90, anchor=CENTER)
tabla1.column("col2", width=150, anchor=CENTER)
tabla1.column("col3", width=100, anchor=CENTER)
tabla1.column("col4", width=100, anchor=CENTER)

tabla1.heading("#0", text="Nombre")
tabla1.heading("col1", text="Edad", anchor=CENTER)
tabla1.heading("col2", text="Especialidad", anchor=CENTER)
tabla1.heading("col3", text="Presente", anchor=CENTER)
tabla1.heading("col4", text="Ausente", anchor=CENTER)

tabla1.insert("", END, text="Maximiliano Ojeda", values=("39", "Docente de Matemática", "28", "0"))
tabla1.insert("", END, text="Jorge Vega", values=("40", "Docente de Religión", "27", "1"))
tabla1.insert("", END, text="Magdalena Hernandez", values=("45", "Docente de Lenguaje", "26", "2"))

tabla1.place(x=250, y=100)

# Estilo ttk
estilo = ttk.Style()
estilo.configure('TButton', background='lightblue', padding=(5, 5, 5, 5))

ventana.mainloop()
