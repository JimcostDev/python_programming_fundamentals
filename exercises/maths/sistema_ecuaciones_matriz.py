# Este script resuelve un sistema de ecuaciones lineales utilizando matrices en Python
import numpy as np
import fractions
np.set_printoptions(formatter={'all': lambda x: str(
    fractions.Fraction(x).limit_denominator())})
# Matriz A
A = np.array([[1,1,1], [2,0,1], [1,2,0]])
# Vector b, terminos independientes
b = np.array([2,1,5])

try:
    # calculamos el determinante:
    determinante = np.linalg.det(A)
    print(f'El determinante es: {round(determinante,2)}')
    print()
    # matriz no singular
    if determinante != 0:
        print('Solución del sistema:')
        x = np.linalg.solve(A, b)
        print(x)
        print()

        print('Comprobamos que A * x = b')
        print(np.matmul(A, x))
    else:
        print('La matriz es singular')
except Exception as e:
    print(f'Ha ocurrido una excepción: {e}')
