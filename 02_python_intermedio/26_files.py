# abrir un archivo
file = open('./text.txt')

# # leer completamente
# print(file.read())

# # leer linea a linea
# print(file.readline())
# print(file.readline())

# leer con for
for line in file:
    print(line)

# cerrar archivo
file.close()

# con esta instrucción se cierra automaticamente
with open('./text.txt') as file:
    for line in file:
        print(line)