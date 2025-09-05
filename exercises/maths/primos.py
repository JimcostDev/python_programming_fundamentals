'''
En matemáticas, un número primo es un número natural
mayor que 1 que tiene únicamente dos divisores 
positivos distintos: él mismo y el 1 (a exepcion del 1).
'''

#declarar variables
numero = int(input("Digite número: "))
contar = int()
print ("Los números primos entre 1 y {} son: ".format(numero))

#logica
for i in range(1, numero+1):
  contar = 0
  for j in range(1,i+1):
    if i%j == 0:
      contar += 1  
  if contar == 2:
     print(i) #imprimir en patalla los números primos
    