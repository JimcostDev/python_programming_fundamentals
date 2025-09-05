"""
simular un ejercicio de potenciacón matematica
"""
base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
acumular = 1

for i in range(exponente):
    acumular = acumular * base
print('el resultado es: {}'.format(acumular))
