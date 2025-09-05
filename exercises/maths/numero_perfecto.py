"""
los números perfectos son aquellos enteros positivos iguales a la suma de sus divisores positivos, 
sin contarse el mismo número.
    ejemplo: 
    el 6, ya que 1+2+3 = 6
    
Nota: Hasta la fecha se han encontrado 51 números pefectos 
"""

## version 1 ##
# Función que determina si un numero es perfecto o no
def esPerfecto(numero):
    if numero <= 5:
        return False
    contar = []
    for n in range(1, numero):
        if numero % n == 0:
            contar.append(n)
    suma = sum(contar)
    if suma == numero:
        return True
    else:
        return False

def run_version_1():
    hasta = int(input('Ingrese el número límite (hasta) para buscar los números perfectos hasta ese número dado: '))
    lista_perfectos = []
    for n in range(5, hasta):
        if esPerfecto(n):
            lista_perfectos.append(n)

    print()
    print(lista_perfectos)
    print(f'Existen {len(lista_perfectos)} números perfectos hasta el número {hasta}.')

## version 2 ##
def es_numero_perfecto(numero):
    suma_divisores = sum([i for i in range(1, numero) if numero % i == 0])
    return suma_divisores == numero

def imprimir_numeros_perfectos(limite):
    for numero in range(1, limite + 1):
        if es_numero_perfecto(numero):
            print(numero)

def run_version_2():
    limite = int(input("Introduce el límite: "))
    imprimir_numeros_perfectos(limite)

def main():
    print("Seleccione la versión a ejecutar:")
    print("1. Versión 1")
    print("2. Versión 2")
    opcion = int(input("Ingrese el número de la versión: "))

    if opcion == 1:
        run_version_1()
    elif opcion == 2:
        run_version_2()
    else:
        print("Opción no válida")

if __name__ == '__main__':
    main()