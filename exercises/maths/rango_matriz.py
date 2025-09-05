# Este script en Python utiliza la biblioteca NumPy para 
# calcular el rango de una matriz dada. Primero, define una matriz A y 
# la imprime en pantalla. Luego, usa la función np.linalg.matrix_rank() 
# para determinar el rango de la matriz y muestra el resultado.

import numpy as np
A = np.array([[1,2,3,4], [0,2,-1,5], [0,0,3,7]])
print(A)
resultado = np.linalg.matrix_rank(A) # Calcula el rango de la matriz A
print(resultado)