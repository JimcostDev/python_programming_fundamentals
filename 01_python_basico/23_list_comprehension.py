numeros = []
for elemento in range(1, 11):
    numeros.append(elemento * 2)

print(numeros)

# list comprehension
numeros_2 = [elemento * 2 for elemento in range(1, 11)] 
print(numeros)


pares = []
for elemento in range(1, 11):
    if elemento % 2 == 0:
        pares.append(elemento * 3) # pares
print(pares)

pares_2 = [elemento * 3 for elemento in range(1, 11) if elemento % 2 == 0]
print(pares_2)

# Crear una nueva lista con los números pares de la lista original, y 'No par' para los impares
numeros_par_o_no_par = ['Par' if num % 2 == 0 else 'No par' for num in numeros]
print(numeros_par_o_no_par)  