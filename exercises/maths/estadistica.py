# este algoritmo lo cree cuando estudiba estadistica y necesitaba ordenar listas
lista = [0, 10, 0, 0, 0, 1, 1, 1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,4,4]
cantidad = len(lista)
lista.sort()#ordenar la lista
print(lista)
print("Total de datos(N): {}".format(cantidad))
#sumar elementos de la lista
suma = 0
for item in lista:
    suma = suma + item
print("la suma de los datos es: {} ".format(suma))
#hallar promedio
promedio = suma/cantidad
print("El promedio es: {}".format(promedio))