from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import PIL.Image

ventana = tk.Tk()
ventana.title("Menu principal - DocWar 1.0")
ventana.geometry("900x500")
ventana.configure(bg="lightblue")

image = PIL.Image.open("DocWare1.0.png")
image = image.resize((175,175), PIL.Image.Resampling.LANCZOS)

img = ImageTk.PhotoImage(image)
lbl_img = Label(ventana, image=img) 
lbl_img.place(x=30,y=30)

#Descripción del software abajo del logo (Doc War)
etiqueta1 = Label(ventana, text="Sistema de gestión", font=("Arial", 15, 'bold'), bg='lightblue')
etiqueta1.place(x=25, y=215)

etiqueta1 = Label(ventana, text="en Asistencias", font=("Arial", 15, 'bold'), bg='lightblue')
etiqueta1.place(x=25, y=250)

#Texto 
Subtitulo1 = Label(ventana, text="Información de los Usuarios", font=("Arial", 20, 'bold'), bg='lightblue')
Subtitulo1.place(x=350, y=25)

#Barra de búsqueda
text_busqueda = tk.StringVar()

entrada_busqueda = tk.Entry(ventana, textvariable=text_busqueda)
entrada_busqueda.pack(side="right", anchor="n", padx=100, pady=65, ipadx=189, ipady=8)

#Tabla de información sobre los funcionarios
tabla1 = ttk.Treeview(ventana,columns=("col1","col2","col3","col4"))
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

tabla1.insert("",END,text="Maximiliano Ojeda", values=("39","Docente de Matemática","28","0"))
tabla1.insert("",END,text="Jorge Vega", values=("40","Docente de Religión","27","1"))
tabla1.insert("",END,text="Magdalena Hernandez", values=("45","Docente de Lenguaje","26","2"))


tabla1.place(x=250, y=100)

# Botones
add_button = tk.Button(ventana, text="Agregar Docente", font=("Arial", 12), bg="crimson", fg="black")
add_button.place(x=200, y=350)


edit_button = tk.Button(ventana, text="Editar Información", font=("Arial", 12), bg="yellow", fg="black")
edit_button.place(x=690, y=350)

# Boton docente
docente_button = tk.Button(ventana, text="    Entrar    ", font=("Arial", 12), bg="cyan", fg="black")
docente_button.place(x=690, y=420)

ventana.mainloop()