'''
while True:
    print('Mientras la condicon sea "True" el bloque de codigo se va a ejecutar')
    # esto es un ciclo infinito porque siempre esta en True
    # es muy utilizado cuando no se conocen el numero de iteraciones que vamos a realizar
'''
# condición
contador = 0
while contador < 10:
    print(contador)
    contador += 1

# ejemplo practico
numero_secreto = 10
print('------ ADIVINA EL NÚMERO -----')
while True:
    adivina = int(input('Escribe el número => '))
    if adivina == numero_secreto:
        break # romper la ejecución del ciclo (stop)
