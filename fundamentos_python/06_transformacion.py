nombre = "Ronaldo"
print(type(nombre))
nombre = 12
print(type(nombre))
nombre = True
print(type(nombre))

print("Ronaldo" + " Jimenez") #concatenar
print(10 + 20)
print("Ronaldo" + "12")

edad = 12 # int
print("Mi edad es " + str(edad))
print(f"Mi edad es {edad}") # format

edad = input('Escribe tu edad => ')
print(type(edad)) #str
edad = int(edad)
print(type(edad)) #int
edad += 10 # edad = edad + 10
print(f'Tu edad en 10 años será¡ {edad}')
