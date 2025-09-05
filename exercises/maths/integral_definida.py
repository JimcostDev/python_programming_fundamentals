# Este script en Python utiliza la biblioteca SciPy para 
# calcular la integral definida de una función matemática 
# en un intervalo específico. Se define una función cuadrática, y
# luego se integra numéricamente entre los límites a  y b usando spi.quad()

# pip install scipy numpy
import scipy.integrate as spi 
import numpy as np

def f(x):
    return (-x**2) - (2*x) + (8)

pi = np.pi
a = -4
b = -3

result, error = spi.quad(f, a, b)
print(round(result,2))
