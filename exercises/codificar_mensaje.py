"""
    # Construye un mensaje de 15 letras. Codifícalo usando la matriz 
    y la transformación lineal. Registra el procedimiento de codificación paso a paso, 
    así como la cadena de dígitos resultante.
"""
import numpy as np
#Definición del mensaje
mensaje = 'Ronaldo Jimenez'

#Obtiene la posición de cada letra del mensaje en el alfabeto
letras = []
for letra in mensaje:
    letras.append(ord(letra) - 64)
print()
print(letras)

#Conforma los vectores para la codificación
x1 =  np.array(letras[0:3])
x2 =  np.array(letras[3:6])
x3 =  np.array(letras[6:9])
x4 =  np.array(letras[9:12])
x5 =  np.array(letras[12:15])

#Matriz A
A = np.array([[3,2,1],[0,1,1],[1,1,2]])

#Transformación lineal, Ax
x1_cod = np.matmul(A, x1)
x2_cod = np.matmul(A, x2)
x3_cod = np.matmul(A, x3)
x4_cod = np.matmul(A, x4)
x5_cod = np.matmul(A, x5)

#Presentación del mensaje codificado
mensaje_cod = np.append(x1_cod, [x2_cod, x3_cod, x4_cod, x5_cod])
lista_mensaje_cod = []
for i in mensaje_cod:
    lista_mensaje_cod.append(i)
#mensaje_cod = " ".join([str(i) for i in mensaje_cod])
print(lista_mensaje_cod)

# SOLUCION
#Mensaje codificado
y1_cod = np.array(lista_mensaje_cod[0:3])
y2_cod = np.array(lista_mensaje_cod[3:6])
y3_cod = np.array(lista_mensaje_cod[6:9])
y4_cod = np.array(lista_mensaje_cod[9:12])
y5_cod = np.array(lista_mensaje_cod[12:15])

#Cálculo de la matriz inversa para el proceso de decodificación
invA = np.linalg.inv(A)

#Decodificación
y1 = np.matmul(invA, y1_cod)
y2 = np.matmul(invA, y2_cod)
y3 = np.matmul(invA, y3_cod)
y4 = np.matmul(invA, y4_cod)
y5 = np.matmul(invA, y5_cod)

#Presentación del mensaje decodificado
mensaje_decod = np.append(y1, [y2, y3, y4, y5])
print('El mensaje decodificado es: ')
for i in mensaje_decod:
    print(chr(int(i + 64)), end="")