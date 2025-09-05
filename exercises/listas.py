#Separar datos tipo numero de textos 
datos = ['Ronaldo','Jimenez',7,27,'COL',1999] 
datos_numeros = [] 
datos_textos = []  

for dato in datos: 
    if type(dato) == int:
        datos_numeros.append(dato) 
    else:
        datos_textos.append(dato)

print(datos_numeros)
print(datos_textos)