from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
from pandastable import Table, TableModel
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Listas globales
nombre, apellido, edad, correo, telefono = [], [], [], [], []

# Variables globales
tabla = None  # Declarar la variable global tabla

# Define las credenciales de inicio de sesión codificadas, estas se pueden cambiar en cualquier momento solo desde el codigo.
usuario_valido = "admin"
contrasena_valida = "password123"

def iniciar_sesion():
    usuario_ingresado = entrada_usuario.get()
    contrasena_ingresada = entrada_contrasena.get()
    
    if usuario_ingresado == usuario_valido and contrasena_ingresada == contrasena_valida:
        ventana_inicio.destroy()  # Cierra la ventana de inicio de sesión
        programa_principal()
    else:
        etiqueta_error.config(text="Usuario o contraseña incorrectos")
        print("Inicio de sesión fallido")

def programa_principal():
    global txtNombre, txtApellido, txtEdad, txtCorreo, txtTelefono, tabla  # Hacer que la variable 'tabla' sea global

    # Crear la ventana principal
    ventana = Tk()
    ventana.title('Guardar datos en Excel')
    ventana.geometry('800x600')
    ventana.resizable(1, 1)
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(0, weight=1)
    
    #Configuramos todo el estilo de los botones del modulo tkk, en la funcion principal
    estilo = ttk.Style()
    estilo.configure('TButton', padding=6, relief="flat", font=('Arial', 12))

    frame1 = Frame(ventana, bg='lightgray', padx=20, pady=20)
    frame1.grid(row=0, column=0, sticky='nsew')
    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0, weight=1)

    frame2 = Frame(ventana, bg='lightgray',padx=20, pady=20)
    frame2.grid(row=0, column=1, sticky='nsew')
    frame2.rowconfigure(0, weight=1)
    frame2.columnconfigure(0, weight=1)

    lblNombre = Label(frame1, text='Nombre', font=('Arial', 12))
    lblNombre.grid(row=0, column=0, padx=10, pady=20)
    txtNombre = Entry(frame1, font=('Arial', 12))
    txtNombre.grid(row=0, column=1)

    lblApellido = Label(frame1, text='Apellido', font=('Arial', 12))
    lblApellido.grid(row=1, column=0, padx=10, pady=20,sticky='w')
    txtApellido = Entry(frame1,  font=('Arial', 12))
    txtApellido.grid(row=1, column=1)

    lblEdad = Label(frame1, text='Edad', font=('Arial', 12))
    lblEdad.grid(row=2, column=0, padx=10, pady=20,sticky='w')
    txtEdad = Entry(frame1, font=('Arial', 12))
    txtEdad.grid(row=2, column=1)

    lblCorreo = Label(frame1, text='Correo', font=('Arial', 12))
    lblCorreo.grid(row=3, column=0, padx=10, pady=20,sticky='w')
    txtCorreo = Entry(frame1, font=('Arial', 12))
    txtCorreo.grid(row=3, column=1)

    lblTelefono = Label(frame1, text='Telefono', font=('Arial', 12))
    lblTelefono.grid(row=4, column=0, padx=10, pady=20,sticky='w')
    txtTelefono = Entry(frame1, font=('Arial', 12))
    txtTelefono.grid(row=4, column=1)

    btnAgregar = Button(frame1, width=20, font=('Arial', 12, 'bold'), text='Agregar',
                        bg='orange', bd=5, command=agregar_datos)
    btnAgregar.grid(row=5, columnspan=2, padx=10, pady=20)

    # Elementos del Frame2
    lblArchivo = Label(frame2, text='Contenido', width=25, bg='gray16',
                       font=('Arial', 12, 'bold'), fg='white')
    lblArchivo.grid(row=0, column=0, padx=10, pady=10)

    tabla = ttk.Treeview(frame2, columns=('Apellidos', 'Edad', 'Correo', 'Telefono'))
    tabla.grid(row=1, column=0)

    tabla.column('#0', width=140)
    tabla.column('Apellidos', width=80, anchor='center')
    tabla.column('Edad', width=80, anchor='center')
    tabla.column('Correo', width=80, anchor='center')
    tabla.column('Telefono', width=80, anchor='center')

    tabla.heading('#0', text='Nombres', anchor='center')
    tabla.heading('Apellidos', text='Apellidos', anchor='center')
    tabla.heading('Edad', text='Edad', anchor='center')
    tabla.heading('Correo', text='Correo', anchor='center')
    tabla.heading('Telefono', text='Telefono', anchor='center')

    btnGuardar = Button(frame2, width=20, font=('Arial', 12, 'bold'), text='Mostrar', bg='green2', bd=5,
                        command=mostrar_datos)
    btnGuardar.grid(row=2, column=0, padx=10, pady=10)

    btnEliminar = Button(frame2, width=20, font=('Arial', 12, 'bold'), text='Eliminar', bg='red', bd=5,
                         command=eliminar_seleccionado)
    btnEliminar.grid(row=3, column=0, padx=10, pady=10)

    # Creación de la barra de menú/falta finalizarla
    menu_bar = Menu(ventana)
    ventana.config(menu=menu_bar)

    archivo_menu = Menu(menu_bar)
    menu_bar.add_cascade(label='Archivo', menu=archivo_menu)
    archivo_menu.add_command(label='Salir', command=ventana.quit)

    #ventana.mainloop()

def agregar_datos():
    global nombre, apellido, edad, correo, telefono
    try:
        nombre.append(txtNombre.get())
        apellido.append(txtApellido.get())
        edad.append(txtEdad.get())
        correo.append(txtCorreo.get())
        telefono.append(txtTelefono.get())

        # Guardar los datos en un archivo CSV
        with open('datos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([txtNombre.get(), txtApellido.get(), txtEdad.get(), txtCorreo.get(), txtTelefono.get()])
        limpiar()
    except Exception as e:
        print("Error al agregar datos:", str(e))

def limpiar():
    txtNombre.delete(0, END)
    txtApellido.delete(0, END)
    txtEdad.delete(0, END)
    txtCorreo.delete(0, END)
    txtTelefono.delete(0, END)

def mostrar_datos():
    # Limpia las listas globales antes de cargar los datos
    global nombre, apellido, edad, correo, telefono
    try:
        nombre, apellido, edad, correo, telefono = [], [], [], [], []

        # Limpia la tabla
        tabla.delete(*tabla.get_children())

        # Cargar los datos desde el archivo CSV
        with open('datos.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                nombre.append(row[0])
                apellido.append(row[1])
                edad.append(row[2])
                correo.append(row[3])
                telefono.append(row[4])

        for i in range(len(nombre)):
            tabla.insert('', END, text=nombre[i], values=(apellido[i], edad[i], correo[i], telefono[i]))
    except Exception as e:
        print("Error al mostrar datos:", str(e))

def eliminar_seleccionado():
    global nombre, apellido, edad, correo, telefono
    try:
        seleccion = tabla.selection()  # Obtiene el elemento seleccionado en la tabla
        if seleccion:
            # Obtiene el índice del elemento seleccionado en la tabla
            index = tabla.index(seleccion)
            # Elimina el elemento seleccionado de las listas globales
            del nombre[index]
            del apellido[index]
            del edad[index]
            del correo[index]
            del telefono[index]

            # Actualiza el archivo CSV con los datos actualizados
            with open('datos.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                for i in range(len(nombre)):
                    writer.writerow([nombre[i], apellido[i], edad[i], correo[i], telefono[i]])

            # Limpia la tabla y vuelve a mostrar los datos actualizados
            tabla.delete(*tabla.get_children())
            mostrar_datos()
    except Exception as e:
        print("Error al eliminar seleccionado:", str(e))

# Crear la ventana de inicio de sesión
ventana_inicio = Tk()
ventana_inicio.title("Inicio de Sesión")
ventana_inicio.geometry("300x200")

etiqueta_inicio = Label(ventana_inicio, text="Por favor, inicia sesión")
etiqueta_inicio.pack(pady=10)

etiqueta_usuario = Label(ventana_inicio, text="Usuario:")
etiqueta_usuario.pack()
entrada_usuario = Entry(ventana_inicio)
entrada_usuario.pack()

etiqueta_contrasena = Label(ventana_inicio, text="Contraseña:")
etiqueta_contrasena.pack()
entrada_contrasena = Entry(ventana_inicio, show="*")
entrada_contrasena.pack()

boton_iniciar_sesion = Button(ventana_inicio, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack(pady=10)

etiqueta_error = Label(ventana_inicio, text="", fg="red")
etiqueta_error.pack()

ventana_inicio.mainloop()