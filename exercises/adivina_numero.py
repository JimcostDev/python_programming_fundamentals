
"""
tines 3 intentos para adivinar un número aleatorio del 1 al 10, suerte.
"""
from random import randint, uniform, random
numero = randint(0, 10)
# contador
intentos = 0
while True:
    adivina = int(input('Escribe un número, solo tienes 3 intentos: '))
    intentos = intentos + 1
    if(intentos == 3):
        print('Fallaste')
        break
    else:
        if (adivina == numero):
            print('Felecidades, adivinaste')
            break
        
            
