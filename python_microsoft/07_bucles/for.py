
# Este es un bucle for de ejemplo que hace una cuenta atrás, de 4 a 0:
from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")

"""
El bucle for es una instrucción con cinco partes importantes:

    1. La palabra for, seguida de un espacio.
    2. El nombre de la variable que quiere crear para cada valor de la secuencia (number).
    3. La palabra in, entre espacios.
    4. El nombre de la lista (countdown, en el ejemplo anterior) u objeto iterable que quiere recorrer en bucle, seguido de dos puntos (:).
    5. El código que quiere ejecutar para cada elemento del objeto iterable, separado por espacios en blanco anidados.
"""

