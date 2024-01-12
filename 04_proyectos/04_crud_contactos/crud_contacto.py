import pyodbc #pip install pyodbc
from tabulate import tabulate #pip install tabulate

# Configurar la conexión a SQL Server
server = '.\LOCAL'
database = 'Test'
username = 'jimcostdev'
password = 'xxxxx'

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
)
cursor = conn.cursor()

# Crear un contacto
def crear_contacto(nombre, apellido, telefono, correo):
    try:
        cursor.execute("EXEC [dbo].[pa_CrearContacto_basico] @nombre=?, @apellido=?, @telefono=?, @correo=?", 
                       nombre, apellido, telefono, correo)
        conn.commit()
        print("El contacto se creó exitosamente.")
    except pyodbc.Error as e:
        print("Error al crear el contacto:", e)

# Actualizar un contacto
def actualizar_contacto(id, nombre, apellido, telefono, correo):
    try:
        cursor.execute("EXEC [dbo].[pa_ActualizarContacto_basico] @ID=?, @nombre=?, @apellido=?, @telefono=?, @correo=?", 
                       id, nombre, apellido, telefono, correo)
        conn.commit()
        print("El contacto se actualizó correctamente.")
    except pyodbc.Error as e:
        print("Error al actualizar el contacto:", e)

# Eliminar un contacto
def eliminar_contacto(id):
    try:
        cursor.execute("EXEC [dbo].[pa_EliminarContacto_basico] @ID=?", id)
        conn.commit()
        print("El contacto se eliminó correctamente.")
    except pyodbc.Error as e:
        print("Error al eliminar el contacto:", e)

# Consultar todos los contactos
def consultar_contactos():
    try:
        cursor.execute("EXEC [dbo].[pa_ConsultarContactos_basico]")
        rows = cursor.fetchall()

        if len(rows) > 0:
            print("Contactos existentes:")
            contactos = format_contactos(rows)
            print(contactos)
        else:
            print("No se encontraron contactos.")
    except pyodbc.Error as e:
        print("Error al consultar los contactos:", e)

# Formatear los contactos en una cadena
def format_contactos(rows):
    headers = ["ID", "Nombre", "Apellido", "Teléfono", "Correo"]
    contactos = tabulate(rows, headers, tablefmt="grid")
    return contactos

# Función para mostrar las opciones CRUD y realizar la operación seleccionada
def opciones_crud():
    while True:
        print("---- Opciones CRUD ----")
        print("1. Crear contacto")
        print("2. Actualizar contacto")
        print("3. Eliminar contacto")
        print("4. Consultar contactos")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            apellido = input("Ingrese el apellido del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            correo = input("Ingrese el correo del contacto: ")
            crear_contacto(nombre, apellido, telefono, correo)
        elif opcion == "2":
            id = input("Ingrese el ID del contacto a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del contacto: ")
            apellido = input("Ingrese el nuevo apellido del contacto: ")
            telefono = input("Ingrese el nuevo teléfono del contacto: ")
            correo = input("Ingrese el nuevo correo del contacto: ")
            actualizar_contacto(id, nombre, apellido, telefono, correo)
        elif opcion == "3":
            id = input("Ingrese el ID del contacto a eliminar: ")
            eliminar_contacto(id)
        elif opcion == "4":
            consultar_contactos()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")


def main():
    try:
        # EJECUTAR PROGRAMA
        opciones_crud()
    finally:
        # Cerrar la conexión
        conn.close()

if __name__ == "__main__":
    main()