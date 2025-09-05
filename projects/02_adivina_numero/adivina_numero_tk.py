import random
import tkinter as tk
from tkinter import messagebox

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Función para verificar el número ingresado por el jugador
def verificar_numero():
    numero = int(entry.get())
    if numero == numero_secreto:
        messagebox.showinfo("¡Felicidades!", "¡Adivinaste el número!")
        ventana.destroy()
    elif numero < numero_secreto:
        messagebox.showinfo("Incorrecto", "El número es mayor. Intenta de nuevo.")
    else:
        messagebox.showinfo("Incorrecto", "El número es menor. Intenta de nuevo.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Adivina el número")

# Etiqueta y entrada de texto
label = tk.Label(ventana, text="Adivina el número (entre 1 y 10):")
label.pack()
entry = tk.Entry(ventana)
entry.pack()

# Botón de verificar
boton = tk.Button(ventana, text="Verificar", command=verificar_numero)
boton.pack()

# Iniciar la ventana principal
ventana.mainloop()