"""
Este programa realiza una suma recursiva, es decir si el numero es 4, su resultado es 10,
ya que recursivamente hace lo siguiente 4+3+2+1 = 10
"""

def suma_recursiva(num_items):
    suma = 0
    # caso base
    if num_items == 1:
        suma = 1
    # caso general
    else:
        suma = num_items+suma_recursiva(num_items-1)
    return suma


def run():
    while True:
        try:
            result = suma_recursiva(int(input('ingrese un nùmero positivo: ')))
            print('la suma es: {} '.format(result))
        except RecursionError:
            print('El número debe ser positivo')


if __name__ == '__main__':
    run()
