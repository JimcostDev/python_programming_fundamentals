
# diccionario = {llave: valor}

persona = {
  'ID': "1234",
  'nombre': 'Ronaldo',
  'apellido': 'Jimenez',
  'edad': 23,
  'lenguajes': ['Python', 'Javascript', 'Go']
}
print(persona)
print()

# actualizar valor
persona['nombre'] = 'jimcostdev'
persona['edad'] += 5
persona['lenguajes'].append('C#') 
print(persona)
print()

# eliminar un valor
del persona['apellido']

# eliminar con pop() - Espera recibir una llave como parametro
persona.pop('ID')
print(persona)

print('items:')
print(persona.items())
print(type(persona.items()))
print()

print('keys:')
print(persona.keys())
print(type(persona.keys()))
print()

print('values:')
print(persona.values())
print(type(persona.values()))
print()

# for clave, valor in persona.items():
#      print(f' clave : {clave}, valor: {valor}')