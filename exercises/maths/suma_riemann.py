# Este script en Python calcula la suma de Riemann para aproximar 
# la integral de una función en un intervalo dado. Se implementan 
# tres aproximaciones: izquierda, superior y punto medio, utilizando 
# un número determinado de subintervalos. Luego, se multiplica cada 
# suma por el ancho del subintervalo para obtener la aproximación final de la integral.
import numpy as np
# Definir la función a integrar
def f(x):
    return (-x**2) + ((3*x)/2) + 4

# Definir el intervalo [a, b]
pi = np.pi
a = -1.38
b = 2.88

# Definir el número de subintervalos
n = 1000

# Calcular el ancho de cada subintervalo
dx = (b - a) / n

# Calcular la suma de Riemann izquierda
left_sum = 0
for i in range(n):
    left_sum += f(a + i*dx)

# Calcular la suma de Riemann superior
upper_sum = 0
for i in range(1, n+1):
    upper_sum += f(a + i*dx)

# Calcular la suma de Riemann punto medio
mid_sum = 0
for i in range(n):
    mid_sum += f(a + (i+0.5)*dx)

# Multiplicar por el ancho del subintervalo
left_sum *= dx
upper_sum *= dx
mid_sum *= dx

# Imprimir los resultados
print("Suma de Riemann izquierda:", left_sum)
print("Suma de Riemann superior:", upper_sum)
print("Suma de Riemann punto medio:", mid_sum)