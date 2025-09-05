import os
import tkinter as tk
from tkinter import messagebox
import subprocess

def crear_y_ejecutar_bat():
    try:
        # Ruta y nombre del archivo .bat en la carpeta de documentos del usuario
        ruta_archivo_bat = os.path.expanduser("~\\Documents\\hola.bat")
        
        # Escribir el contenido del archivo .bat
        with open(ruta_archivo_bat, "w") as archivo_bat:
            archivo_bat.write("@echo off\nstart chrome https://www.jimcostdev.com")

        # Ejecutar el archivo .bat
        subprocess.Popen([ruta_archivo_bat], shell=True)

        # Mostrar el mensaje de activación exitosa
        messagebox.showinfo("Activación Exitosa", "¡Enhorabuena! Tu software ha sido activado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar el archivo .bat: {str(e)}")

def main():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Activador")
    ventana.geometry("400x300")

    # Mensaje de bienvenida
    mensaje_bienvenida = tk.Label(ventana, text="¡Bienvenido!\n¿Quieres activar tu app sin costo? ¡Haz clic en el botón de abajo!")
    mensaje_bienvenida.pack(pady=20)

    # Crear un botón llamativo para activar
    boton_activar = tk.Button(ventana, text="Activar", bg="green", fg="white", padx=10, pady=5, command=crear_y_ejecutar_bat)
    boton_activar.pack()

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()

if __name__ == "__main__":
    main()
