import random

# CONSTANTES (ID)
PIEDRA = 'PI'
PAPEL = 'PA'
TIJERA = 'TI'

# VARIABLES PARA JUGAR
opciones = (PIEDRA, PAPEL, TIJERA)
usuario = input(''' 
                PIEDRA (PI)
                PAPEL (PA) O 
                TIJERA (TI) 
                => 
                ''')
usuario = usuario.upper()
maquina = random.choice(opciones)
print(f'{usuario} vs {maquina}')


def play(user, machine):
    # Combinaciones en las que el usuario pierde
    perder = {
        (PIEDRA, PAPEL): True,
        (PAPEL, TIJERA): True,
        (TIJERA, PIEDRA): True
    }

    # Combinaciones en las que el usuario gana
    ganar = {
        (PIEDRA, TIJERA): True,
        (PAPEL, PIEDRA): True,
        (TIJERA, PAPEL): True
    }

    if (user, machine) in perder:
        return False
    elif (user, machine) in ganar:
        return True
    else:
        return 'empate'

# EJECUCIÓN
resultado = play(usuario, maquina)

if resultado is True:
    print('Ganador: usuario')
elif resultado is False:
    print('Ganador: maquina')
elif resultado == 'empate':
    print('Empate')
