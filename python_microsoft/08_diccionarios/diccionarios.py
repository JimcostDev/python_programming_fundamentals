"""Los diccionarios son un tipo de estructura de datos que permite almacenar desde str, int, float, hasta listas ( etc)
Se llaman mediante "variable_diccionario = {} ".
Y se añaden tipos de datos mediante variable_diccionario [Asignación] = variable."""
notas = {}
notas['POO'] = float(input('Digite nota de poo:'))
notas['BaseDeDatos'] = float(input('Digite nota de bd:'))
notas['Redes']= float(input('Digite nota de redes:'))

suma_notas = 0
for nota in notas.values():
    suma_notas = suma_notas + nota
    prom = suma_notas / len(notas.values())
    result = prom

print('El promedio es: {}'.format(result))

