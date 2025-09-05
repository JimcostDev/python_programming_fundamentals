def contar_caracteres():
    palabra = input("Escribe una palabra o cadena de caracteres: ")
    total_caracteres = len(palabra)
    print("la cadena {}, tiene {} caracteres".format(palabra,total_caracteres))
    
if __name__ == '__main__':
    contar_caracteres()
    print('Fin del progrma')
