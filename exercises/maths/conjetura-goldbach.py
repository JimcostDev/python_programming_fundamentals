'''
---- CONJETURA DE GOLDBACH ----
Todo número par mayor que 2 se puede expresar como suma de dos números primos.

Para el número 14 tendríamos: 3 y 11, 7 y 7
(1 y 13 no valdrian, ya que el uno no es considerado un primo)

Hacer un programa que muestre todas las parejas de primos en las que se puede
expresar un número par mayor que 2.
'''
# función que me permite saber si un número es primo o no
def es_primo(n):
    if n < 2:
        return False
    for i in range(2,n): # se excluye el  1 y el mismo numero
        if n % i == 0:
            return False
    return True

# uniendo las parejas 
num = int(input("Número par mayor que 2: "))
if num % 2 == 0 and num > 2: #condición para verificar que el numero sea par y mayor que 2
  encontrado = False
  for a in range (2, num):
    if es_primo(a):
      #se toma num(14) y se le resta el primer numero primo a(3) y si el resultado b(11) es un numero primo, se forma una pareja (a,b) y asi hasta terminar el ciclo.
      b = num - a 
      if es_primo(b):
        encontrado = True
        if a <= b: #condición para evitar que se repitan las parejas
          print("Primos",a,b) #mostrar en pantalla las parejas

  if not encontrado:
    print("No se ha encontrado ninguna pareja")
else:
  print ("No es un numero valido")
