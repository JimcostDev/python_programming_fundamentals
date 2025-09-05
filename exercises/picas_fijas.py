"""
    El juego de "Picas y Fijas" consiste en adivinar un número de varias cifras, en este caso solo 4. 
    Cada vez que se propone una combinación de dígitos, se reciben pistas en forma de "picas" y "fijas". 
    Las "picas" indican dígitos correctos pero en posiciones incorrectas, mientras que las "fijas" 
    representan dígitos correctos y en las posiciones correctas. Utilizando estas pistas, se 
    debe deducir la combinación oculta con la menor cantidad de intentos posibles. 
    En este programa, se asume que los dígitos no se repiten.
"""

# ----------------------- VERSION 1 ----------------------- #

# importar la función sample del módulo random
from random import sample

intentos = 0
cifras = 4
jugar = True
ganar = False
picas = 0
fijas = 0

def generar_numero_random(cantidadCifras):
    digitos = list(range(10))
    numeroSecreto = sample(digitos, cantidadCifras)
    return numeroSecreto

def retornar_picas_fijas(numero_usuario):
    global fijas, picas
    fijas = 0
    picas = 0
    for digito in range(cifras):
        if numero_usuario[digito] in numero_secreto:
            if numero_usuario[digito] == numero_secreto[digito]:
                fijas = fijas + 1
            else:
                picas = picas + 1
    print(f'Fijas: {fijas}, Picas: {picas}. Llevas: {intentos} intentos.')

numero_secreto = generar_numero_random(cifras)
#print(numero_secreto) # Descomentar para ver el número secreto

while jugar:
    numero_jugador = input(f'Ingresa un número de {cifras} cifras: ')
    cantidad_cifras = len(numero_jugador)
    if cantidad_cifras == 4:
        numero = list(numero_jugador)
        numero = [int(num) for num in numero]
        intentos = intentos + 1

        if numero == numero_secreto:
            ganar = True
            jugar = False
        else:
            retornar_picas_fijas(numero)
            if intentos >= 20:
                print('Perdiste')
                jugar = False
    else:
        print('Debe ser un número de 4 cifras')
        intentos = intentos + 1
        if intentos >= 20:
                print('Perdiste')
                jugar = False

def retornar_mensaje(intentos):
    mensajes = [
        "Excelente, ganaste, lo hiciste en {} intentos",
        "Muy bien, ganaste, lo hiciste en {} intentos",
        "Bien, estás progresando, ganaste, lo hiciste en {} intentos",
        "Ganaste, pero puedes mejorar, lo hiciste en {} intentos",
        "Ganaste, pero te demoraste mucho, lo hiciste en {} intentos"
    ]
    
    if ganar:
        if intentos <= 2:
            mensaje_index = 0
        elif intentos <= 4:
            mensaje_index = 1
        elif intentos <= 8:
            mensaje_index = 2
        elif intentos <= 10:
            mensaje_index = 3
        else:
            mensaje_index = 4
        
        mensaje = mensajes[mensaje_index]
        return mensaje.format(intentos)

if ganar:
    mensaje_salida = retornar_mensaje(intentos)
    print(mensaje_salida)
    print(f'El número secreto es: {numero_secreto}')
else:
    mensaje_salida = 'Vuelve a intentarlo'
    print(f'El número secreto era: {numero_secreto}')


# ----------------------- VERSION 2 ----------------------- #
"""
# Importar la función sample del módulo random
from random import sample

# Inicializar variables
intentos = 0
cifras = 4
jugar = True
ganar = False

# Función para generar un número secreto aleatorio de 4 cifras sin repetición
def generar_numero_random(cantidad_cifras):
    digitos = list(range(10))
    return sample(digitos, cantidad_cifras)

# Función para calcular picas y fijas
def retornar_picas_fijas(numero_usuario, numero_secreto):
    fijas = sum(1 for i in range(cifras) if numero_usuario[i] == numero_secreto[i])
    picas = sum(1 for i in range(cifras) if numero_usuario[i] in numero_secreto and numero_usuario[i] != numero_secreto[i])
    print(f'Fijas: {fijas}, Picas: {picas}. Llevas: {intentos} intentos.')
    return fijas

# Generar el número secreto
numero_secreto = generar_numero_random(cifras)
# print(numero_secreto) # Descomentar para ver el número secreto

# Loop principal del juego
while jugar:
    numero_jugador = input(f'Ingresa un número de {cifras} cifras: ')
    if len(numero_jugador) == 4 and numero_jugador.isdigit():
        numero = [int(num) for num in numero_jugador]
        intentos += 1

        if numero == numero_secreto:
            ganar = True
            jugar = False
        else:
            fijas = retornar_picas_fijas(numero, numero_secreto)
            if intentos >= 12:
                print('Perdiste')
                jugar = False
    else:
        print('Debe ser un número de 4 cifras')

# Función para retornar un mensaje según la cantidad de intentos
def retornar_mensaje(intentos):
    mensajes = [
        "Excelente, ganaste, lo hiciste en {} intentos",
        "Muy bien, ganaste, lo hiciste en {} intentos",
        "Bien, estás progresando, ganaste, lo hiciste en {} intentos",
        "Ganaste, pero puedes mejorar, lo hiciste en {} intentos",
        "Ganaste, pero te demoraste mucho, lo hiciste en {} intentos"
    ]
    
    if intentos <= 2:
        mensaje_index = 0
    elif intentos <= 4:
        mensaje_index = 1
    elif intentos <= 8:
        mensaje_index = 2
    elif intentos <= 10:
        mensaje_index = 3
    else:
        mensaje_index = 4
    
    return mensajes[mensaje_index].format(intentos)

# Mostrar el mensaje final
if ganar:
    print(retornar_mensaje(intentos))
    print(f'El número secreto es: {numero_secreto}')
else:
    print('Vuelve a intentarlo')
    print(f'El número secreto era: {numero_secreto}')

"""