#INTERFAZ
import random
IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        ==========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        ==========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
        ==========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        ==========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ==========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
        ==========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
        ==========''', '''
        ''']

WORDS = [
    'balaca',
    'secador',
    'espejo',
    'peineta',
    'gancho',
    'computador',
    'celular',
    'audifono'
]
def random_word():
    index = random.randint(0, len(WORDS) - 1)#acceder al indice de la lista  aleaotriamente, -1 para evitar salirnos del index de la lista
    return WORDS[index]


#con esta funcion mostramos nuestra imagenes
def show_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('_____________________________________')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word) #palabra_escondida. Multiplicamos por el tamaño de la palabra que acabamos de guardar en la variable word
    tries = 0 #contador de intentos(tries)

    while True:
        show_board(hidden_word, tries)
        current_letter = str(input('Escribe una letra: '))

        #logica del juego
        letter_indixes = []
        for letter in range(len(word)):
            if word[letter] == current_letter:#si la letra que ingreso el user es igual a una letra de la palabra, la asignamos a la lista letter_indixes
                letter_indixes.append(letter)

        if len(letter_indixes) == 0:
            tries += 1

        if tries >= 7:
            show_board(hidden_word, tries)
            print('')
            print('Haz perdido, vuelve a intentarlo, la palabra correcta es: {}'.format(word))
            break

        else:
            #remplazar letra por letra
            for letter in letter_indixes:
                hidden_word[letter] = current_letter
            letter_indixes = []#limpiar la lista

            try:
                hidden_word.index('-')
            except ValueError:
                print('')
                print('Felicidades, ganaste. La palabra es {}'.format(word))
                break


if __name__ == '__main__':
    print('B I E N V E N I D O S')
    run()