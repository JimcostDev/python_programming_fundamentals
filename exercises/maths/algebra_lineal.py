
import numpy as np
import fractions
np.set_printoptions(formatter={'all': lambda x: str(
    fractions.Fraction(x).limit_denominator())})

"""
# Matriz B
B = np.array([[10,-5,-5], [5,-12,3], [5,3,-8]])
# Vector d, terminos independientes
d = np.array([12,0,6])



# Matriz A
A = np.array([[7,-5,0], [5,-17,5], [0,5,-7]])
# Vector b, terminos independientes
b = np.array([9, 0, 5])
"""

# Matriz A
A = np.array([[7,-5,0], [5,-17,5], [0,5,-7]])

# Vector b, terminos independientes
b = np.array([9, 0, 5])

try:
    # calculamos el determinante:
    determinante = np.linalg.det(A)
    print(f'El determinante es: {determinante}')
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
