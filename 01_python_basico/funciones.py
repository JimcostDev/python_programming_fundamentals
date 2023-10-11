def suma(x, y):
    resultado = x + y
    return resultado

def perfil(usuario):
    perfiles = []
    for clave, valor in usuario.items():
        perfiles.append((clave, valor))
    return perfiles

usuario = {'ID': "1234",'name': 'Ronaldo','last_name': 'Jimenez','age': 23}
print(perfil(usuario))


usuario = {'ID': "1234",'name': 'Barbara','last_name': 'Gomez','age': 25}
print(perfil(usuario))

print(suma(7,9765))
print(suma(7,6))

