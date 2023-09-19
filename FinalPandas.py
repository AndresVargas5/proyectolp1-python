from tkinter import *
from tkinter import ttk
import csv
from pandastable import Table, TableModel

# Listas globales
nombre, apellido, edad, correo, telefono = [], [], [], [], []

# Variables globales
tabla = None

# Define las credenciales de inicio de sesión codificadas, estas se pueden cambiar en cualquier momento solo desde el código.
usuario_valido = "admin"
contrasena_valida = "password123"

def iniciar_sesion():
    usuario_ingresado = entrada_usuario.get()
    contrasena_ingresada = entrada_contrasena.get()
    
    if usuario_ingresado == usuario_valido and contrasena_ingresada == contrasena_valida:
        ventana_inicio.destroy()
        programa_principal()
    else:
        etiqueta_error.config(text="Usuario o contraseña incorrectos")
        print("Inicio de sesión fallido")

def programa_principal():
    global tabla

    # Crear la ventana principal
    ventana = Tk()
    ventana.title('Guardar datos en Excel')
    ventana.geometry('800x600')
    ventana.resizable(1, 1)
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(0, weight=1)

    frame = Frame(ventana, bg='lightgray', padx=20, pady=20)
    frame.grid(row=0, column=0, sticky='nsew')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    lblEspacio = Label(frame, text='', font=('Arial', 12))
    lblEspacio.grid(row=0, column=0, padx=(10, 5), pady=5, sticky='e')

    lblNombre = Label(frame, text='Nombre:', font=('Arial', 12))
    lblNombre.grid(row=0, column=0, sticky='e')
    txtNombre = Entry(frame, font=('Arial', 12))
    txtNombre.grid(row=0, column=1, padx=(0, 10), pady=5, sticky='w')

    lblApellido = Label(frame, text='Apellido:', font=('Arial', 12))
    lblApellido.grid(row=1, column=0, padx=(10, 5), pady=5, sticky='e')
    txtApellido = Entry(frame, font=('Arial', 12))
    txtApellido.grid(row=1, column=1, padx=(0, 10), pady=5, sticky='w')

    lblEdad = Label(frame, text='Edad:', font=('Arial', 12))
    lblEdad.grid(row=2, column=0, padx=(10, 5), pady=5, sticky='e')
    txtEdad = Entry(frame, font=('Arial', 12))
    txtEdad.grid(row=2, column=1, padx=(0, 10), pady=5, sticky='w')

    lblCorreo = Label(frame, text='Correo:', font=('Arial', 12))
    lblCorreo.grid(row=3, column=0, padx=(10, 5), pady=5, sticky='e')
    txtCorreo = Entry(frame, font=('Arial', 12))
    txtCorreo.grid(row=3, column=1, padx=(0, 10), pady=5, sticky='w')

    lblTelefono = Label(frame, text='Telefono:', font=('Arial', 12))
    lblTelefono.grid(row=4, column=0, padx=(10, 5), pady=5, sticky='e')
    txtTelefono = Entry(frame, font=('Arial', 12))
    txtTelefono.grid(row=4, column=1, padx=(0, 10), pady=5, sticky='w')

    btnAgregar = Button(frame, text='Agregar', width=20, font=('Arial', 12, 'bold'), bg='orange', bd=5, 
                        command=lambda: agregar_datos(txtNombre, txtApellido, txtEdad, txtCorreo, txtTelefono))
    btnAgregar.grid(row=5, columnspan=2, padx=10, pady=20)

    tabla = ttk.Treeview(frame, columns=('Apellidos', 'Edad', 'Correo', 'Telefono'))
    tabla.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

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

    btnMostrar = Button(frame, text='Mostrar', width=20, font=('Arial', 12, 'bold'), bg='green2', bd=5, command=mostrar_datos)
    btnMostrar.grid(row=7, column=0, padx=10, pady=10)

    btnEliminar = Button(frame, text='Eliminar', width=20, font=('Arial', 12, 'bold'), bg='red', bd=5, command=eliminar_seleccionado)
    btnEliminar.grid(row=7, column=1, padx=10, pady=10)

    menu_bar = Menu(ventana)
    ventana.config(menu=menu_bar)

    archivo_menu = Menu(menu_bar)
    menu_bar.add_cascade(label='Archivo', menu=archivo_menu)
    archivo_menu.add_command(label='Salir', command=ventana.quit)

    ventana.mainloop()

def agregar_datos(nombre_entry, apellido_entry, edad_entry, correo_entry, telefono_entry):
    global nombre, apellido, edad, correo, telefono
    try:
        nombre.append(nombre_entry.get())
        apellido.append(apellido_entry.get())
        edad.append(edad_entry.get())
        correo.append(correo_entry.get())
        telefono.append(telefono_entry.get())

        with open('datos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nombre_entry.get(), apellido_entry.get(), edad_entry.get(), correo_entry.get(), telefono_entry.get()])
        
        limpiar(nombre_entry, apellido_entry, edad_entry, correo_entry, telefono_entry)
    except Exception as e:
        print("Error al agregar datos:", str(e))

def limpiar(nombre_entry, apellido_entry, edad_entry, correo_entry, telefono_entry):
    nombre_entry.delete(0, END)
    apellido_entry.delete(0, END)
    edad_entry.delete(0, END)
    correo_entry.delete(0, END)
    telefono_entry.delete(0, END)

def mostrar_datos():
    global nombre, apellido, edad, correo, telefono
    try:
        nombre, apellido, edad, correo, telefono = [], [], [], [], []

        tabla.delete(*tabla.get_children())

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
        seleccion = tabla.selection()
        if seleccion:
            index = tabla.index(seleccion)
            del nombre[index]
            del apellido[index]
            del edad[index]
            del correo[index]
            del telefono[index]

            with open('datos.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                for i in range(len(nombre)):
                    writer.writerow([nombre[i], apellido[i], edad[i], correo[i], telefono[i]])

            tabla.delete(*tabla.get_children())
            mostrar_datos()
    except Exception as e:
        print("Error al eliminar seleccionado:", str(e))

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