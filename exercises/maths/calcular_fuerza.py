def calcularFuerza(q1,q2,r):
    try:
        carga_1 = q1
        carga_2 = q2
        distantacia = r
        k = 9e9
        F = k * (carga_1 * carga_2) / (distantacia * distantacia)
        return F
    except Exception as e:
        print(f'Ocurrio una excepciíon en la ejecución del programa: {e}')
    
def run():
    try:
        q1 = float(input('Ingrese valor de la carga uno (q1) en coloumb:> '))
        q2 = float(input('Ingrese valor de la carga dos (q2) en coloumb:> '))
        r = float(input('Ingrese valor de la distancia (r) en metros:> '))
        print (f'La fuerza es de: {calcularFuerza(q1,q2,r)}N')
    except Exception as e:
        print(f'Ocurrio una excepciíon en la ejecución del programa: {e}')

if __name__ == '__main__':
    run()