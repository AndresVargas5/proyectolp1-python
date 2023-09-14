from tkinter import * 
from tkinter import ttk
import pandas as pd
import csv
#pip install pandastable, python3 -m pip install pandastable
from pandastable import Table, TableModel

#listas globales
nombre,apellido,edad,correo,telefono=[],[],[],[],[]

#df = pd.DataFrame(columns=['Nombre', 'Apellido', 'Edad', 'Correo', 'Telefono'])para hacerlo con dataframe, pendiente modificar funciones

def agregar_datos():
    global nombre,apellido,edad,correo,telefono
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

def limpiar():
    txtNombre.delete(0,END)
    txtApellido.delete(0,END)
    txtEdad.delete(0,END)
    txtCorreo.delete(0,END)
    txtTelefono.delete(0,END)

def mostrar_datos():
    # Limpia las listas globales antes de cargar los datos
    global nombre, apellido, edad, correo, telefono
    nombre, apellido, edad, correo, telefono = [], [], [], [], []
    
    # Limpia la tabla
    tabla.delete(*tabla.get_children())

    # Cargar los datos desde el archivo CSV
    try:
        with open('datos.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                nombre.append(row[0])
                apellido.append(row[1])
                edad.append(row[2])
                correo.append(row[3])
                telefono.append(row[4])
    except FileNotFoundError:
        pass
    
    for i in range(len(nombre)):
        tabla.insert('', END, text=nombre[i], values=(apellido[i], edad[i], correo[i], telefono[i]))

def eliminar_seleccionado():
    global nombre, apellido, edad, correo, telefono
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
    
ventana= Tk()
ventana.title('Guardar datos en excel')
ventana.geometry('800x600')
ventana.resizable(1,1)
ventana.rowconfigure(0, weight=1)  # La primera fila (0) se expandirá ###
ventana.columnconfigure(0, weight=1) ###

frame1= Frame(ventana,bg='gray15')
frame1.grid(row=0,column=0,sticky='nsew')
frame1.rowconfigure(0, weight=1)  # La primera fila (0) de frame1 se expandirá ###
frame1.columnconfigure(0, weight=1)  # La primera columna (0) de frame1 se expandirá ###

frame2= Frame(ventana,bg='gray16')
frame2.grid(row=0,column=1,sticky='nsew')
frame2.rowconfigure(0, weight=1)  # La primera fila (0) de frame2 se expandirá
frame2.columnconfigure(0, weight=1)  # La primera columna (0) de frame2 se expandirá

lblNombre= Label(frame1, text='Nombre', width=10)
lblNombre.grid(row=0,column=0,padx=10, pady=20)
txtNombre=Entry(frame1, width=20, font=('Arial',12))
txtNombre.grid(row=0,column=1)

lblApellido= Label(frame1, text='Apellido', width=10)
lblApellido.grid(row=1,column=0,padx=10, pady=20)
txtApellido=Entry(frame1, width=20, font=('Arial',12))
txtApellido.grid(row=1,column=1)

lblEdad= Label(frame1, text='Edad', width=10)
lblEdad.grid(row=2,column=0,padx=10, pady=20)
txtEdad=Entry(frame1, width=20, font=('Arial',12))
txtEdad.grid(row=2,column=1)

lblCorreo= Label(frame1, text='Correo', width=10)
lblCorreo.grid(row=3,column=0,padx=10, pady=20)
txtCorreo=Entry(frame1, width=20, font=('Arial',12))
txtCorreo.grid(row=3,column=1)

lblTelefono= Label(frame1, text='Telefono', width=10)
lblTelefono.grid(row=4,column=0,padx=10, pady=20)
txtTelefono=Entry(frame1, width=20, font=('Arial',12))
txtTelefono.grid(row=4,column=1)

btnAgregar=Button(frame1,width=20,font=('Arial',12,'bold'),text='Agregar', 
                  bg='orange',bd=5,command=agregar_datos)
btnAgregar.grid(row=5,columnspan=2,padx=10,pady=20)

#Elementos del Frame2
lblArchivo=Label(frame2,text='Contenido',width=25,bg='gray16',
                 font=('Arial',12,'bold'),fg='white')
lblArchivo.grid(row=0,column=0,padx=10,pady=10)

tabla = ttk.Treeview(frame2,columns=( 'Apellidos','Edad','Correo','Telefono'))
tabla.grid(row=1,column=0)

tabla.column('#0',width=140)
tabla.column('Apellidos',width=80,anchor='center')
tabla.column('Edad',width=80,anchor='center')
tabla.column('Correo',width=80,anchor='center')
tabla.column('Telefono',width=80,anchor='center')

tabla.heading('#0', text='Nombres', anchor='center')
tabla.heading('Apellidos', text='Apellidos', anchor='center')
tabla.heading('Edad', text='Edad', anchor='center')
tabla.heading('Correo', text='Correo', anchor='center')
tabla.heading('Telefono', text='Telefono', anchor='center')

btnGuardar=Button(frame2,width=20,font=('Arial',12,'bold'),text='Mostrar',bg='green2',bd=5,command=mostrar_datos)
btnGuardar.grid(row=2,column=0,padx=10,pady=10)

btnEliminar = Button(frame2, width=20, font=('Arial', 12, 'bold'), text='Eliminar', bg='red', bd=5, command=eliminar_seleccionado)
btnEliminar.grid(row=3, column=0, padx=10, pady=10)

#Creacion Barra de Menu
barraMenu = Menu(ventana)
ventana.config(menu= barraMenu, width=400, height=400)



ventana.mainloop()