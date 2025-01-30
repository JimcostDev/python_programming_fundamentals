import tkinter as tk
from tkinter import messagebox
import pyodbc
from tabulate import tabulate


# Configuración de la conexión a SQL Server
server = '.\LOCAL'
database = 'Test'
username = 'jimcostdev'
password = 'xxxxx'

# Establecer conexión a la base de datos
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
)
cursor = conn.cursor()

# Crear un contacto
def crear_contacto():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()

    try:
        cursor.execute("EXEC [dbo].[pa_CrearContacto_basico] @nombre=?, @apellido=?, @telefono=?, @correo=?", 
                       nombre, apellido, telefono, correo)
        conn.commit()
        messagebox.showinfo("Éxito", "El contacto se creó exitosamente.")
    except pyodbc.Error as e:
        messagebox.showerror("Error", "Error al crear el contacto: " + str(e))

# Actualizar un contacto
def actualizar_contacto():
    id = entry_id.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()

    try:
        cursor.execute("EXEC [dbo].[pa_ActualizarContacto_basico] @ID=?, @nombre=?, @apellido=?, @telefono=?, @correo=?", 
                       id, nombre, apellido, telefono, correo)
        conn.commit()
        messagebox.showinfo("Éxito", "El contacto se actualizó correctamente.")
    except pyodbc.Error as e:
        messagebox.showerror("Error", "Error al actualizar el contacto: " + str(e))

# Eliminar un contacto
def eliminar_contacto():
    id = entry_id.get()

    try:
        cursor.execute("EXEC [dbo].[pa_EliminarContacto_basico] @ID=?", id)
        conn.commit()
        messagebox.showinfo("Éxito", "El contacto se eliminó correctamente.")
    except pyodbc.Error as e:
        messagebox.showerror("Error", "Error al eliminar el contacto: " + str(e))

# Consultar todos los contactos
def consultar_contactos():
    try:
        cursor.execute("EXEC [dbo].[pa_ConsultarContactos_basico]")
        rows = cursor.fetchall()

        if len(rows) > 0:
            contactos = format_contactos(rows)
            messagebox.showinfo("Contactos existentes", contactos)
        else:
            messagebox.showinfo("Sin resultados", "No se encontraron contactos.")
    except pyodbc.Error as e:
        messagebox.showerror("Error", "Error al consultar los contactos: " + str(e))

# Formatear los contactos en una cadena
def format_contactos(rows):
    headers = ["ID", "Nombre", "Apellido", "Teléfono", "Correo"]
    contactos = tabulate(rows, headers, tablefmt="plain")
    return contactos




# Ventana principal
window = tk.Tk()
window.title("Gestión de contactos")

# Etiquetas y campos de entrada
label_id = tk.Label(window, text="ID:")
label_id.grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(window)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nombre = tk.Label(window, text="Nombre:")
label_nombre.grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(window)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

label_apellido = tk.Label(window, text="Apellido:")
label_apellido.grid(row=2, column=0, padx=10, pady=5)
entry_apellido = tk.Entry(window)
entry_apellido.grid(row=2, column=1, padx=10, pady=5)

label_telefono = tk.Label(window, text="Teléfono:")
label_telefono.grid(row=3, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(window)
entry_telefono.grid(row=3, column=1, padx=10, pady=5)

label_correo = tk.Label(window, text="Correo:")
label_correo.grid(row=4, column=0, padx=10, pady=5)
entry_correo = tk.Entry(window)
entry_correo.grid(row=4, column=1, padx=10, pady=5)

# Botones
btn_crear = tk.Button(window, text="Crear", command=crear_contacto)
btn_crear.grid(row=5, column=0, padx=10, pady=5)

btn_actualizar = tk.Button(window, text="Actualizar", command=actualizar_contacto)
btn_actualizar.grid(row=5, column=1, padx=10, pady=5)

btn_eliminar = tk.Button(window, text="Eliminar", command=eliminar_contacto)
btn_eliminar.grid(row=5, column=2, padx=10, pady=5)

btn_consultar = tk.Button(window, text="Consultar", command=consultar_contactos)
btn_consultar.grid(row=5, column=3, padx=10, pady=5)

# Configuración de los campos y botones según la opción seleccionada
def seleccionar_opcion(opcion):
    if opcion == "crear":
        label_id.grid_remove()
        entry_id.grid_remove()
        btn_crear.grid(row=5, column=0, padx=10, pady=5)
        btn_actualizar.grid_remove()
        btn_eliminar.grid_remove()
    elif opcion == "actualizar":
        label_id.grid(row=0, column=0, padx=10, pady=5)
        entry_id.grid(row=0, column=1, padx=10, pady=5)
        btn_crear.grid_remove()
        btn_actualizar.grid(row=5, column=1, padx=10, pady=5)
        btn_eliminar.grid_remove()
    elif opcion == "eliminar":
        label_id.grid(row=0, column=0, padx=10, pady=5)
        entry_id.grid(row=0, column=1, padx=10, pady=5)
        btn_crear.grid_remove()
        btn_actualizar.grid_remove()
        btn_eliminar.grid(row=5, column=2, padx=10, pady=5)

# Menú de opciones
opcion_var = tk.StringVar(window, "crear")
opcion_var.trace("w", lambda *args: seleccionar_opcion(opcion_var.get()))

radio_crear = tk.Radiobutton(window, text="Crear", variable=opcion_var, value="crear")
radio_crear.grid(row=6, column=0, padx=10, pady=5)

radio_actualizar = tk.Radiobutton(window, text="Actualizar", variable=opcion_var, value="actualizar")
radio_actualizar.grid(row=6, column=1, padx=10, pady=5)

radio_eliminar = tk.Radiobutton(window, text="Eliminar", variable=opcion_var, value="eliminar")
radio_eliminar.grid(row=6, column=2, padx=10, pady=5)

# Mostrar ventana principal
seleccionar_opcion("crear")  # Opción por defecto: crear
window.mainloop()

# Cerrar la conexión
conn.close()
