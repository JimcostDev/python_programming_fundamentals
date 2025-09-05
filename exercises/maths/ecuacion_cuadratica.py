"""
    Ax^2 + Bx + C = 0
    A != 0

    * Todas las ecuaciones se pueden graficar
    * Cuando nos dicen que solucione la ecuación cuadratica, no estan preguntando en donde corta esa ecuación al eje X
    * 3 casos:
        Tiene 2 respuestas cuando corta al eje X 2 veces (x^2 + 8x + 12)
        Tiene 1 respuestas cuando corta al eje X 1 vez (x^2 + 2x + 1)
        Sin solución o sin respuesta, no toca al eje X en ningun punto (3x^2 - 8x +6)

    * Formula general:
        x = -b -/+ sqrt(b^2-4ac)/2a
""" 
from math import sqrt

def ecuacion_cuadratica(a,b,c):
    condicional = b**2 - (4*a*c)
    if condicional > 0:
        x1 = (-b + sqrt(condicional))/(2*a)
        x2 = (-b - sqrt(condicional))/(2*a)
        return (x1, x2)
    elif condicional == 0:
        x1 = -b / (2*a)
        return (x1,)
    else:
        return tuple()

print(ecuacion_cuadratica(1,8,12))
print(ecuacion_cuadratica(1,2,1))
print(ecuacion_cuadratica(3,8,6))