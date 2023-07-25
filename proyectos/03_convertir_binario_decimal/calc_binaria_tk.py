import tkinter as tk

def mostrar_resultado():
    binario = entry_binario.get()
    # Verificar que solo se ingresen 0 y 1
    if not all(bit in ('0', '1') for bit in binario):
        resultado.config(text="¡Error! Ingresa solo valores binarios (0 y 1).")
    else:
        numero_binario = calcular_decimal(binario)
        resultado.config(text=f'El número en decimal es: {numero_binario}')
    
def calcular_decimal(binario):
    bits = list(binario)
    for bit in range(len(bits)):
        bits[bit] = int(bits[bit])

    total = 0
    acumulador = 1
    bits.reverse()
    for bit in range(len(bits)):
        acumulador = acumulador * 2
        bits[bit] = bits[bit] * acumulador // 2
        total += bits[bit]
    return total

# Crear la ventana
ventana = tk.Tk()
ventana.title("Convertidor Binario a Decimal")

# Etiqueta y entrada para ingresar el número binario
label_binario = tk.Label(ventana, text="Número binario:")
label_binario.pack()

entry_binario = tk.Entry(ventana)
entry_binario.pack()

# Botón para realizar la conversión
boton_convertir = tk.Button(ventana, text="Convertir", command=mostrar_resultado)
boton_convertir.pack()

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Ejecutar la ventana
ventana.mainloop()
