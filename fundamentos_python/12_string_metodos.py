texto = 'Ya se programar en Python'
print(texto)

if 'Python' in texto:
  print('Python es un lenguaje genial!!')
else:
  print('Haz elegido otro lenguaje, esta bien')

size = len(texto) # tamaño
print(size)

print(texto.upper()) # mayusculas
print(texto.lower()) # minusculas
print(f"En el texto aparece {texto.count('a')} veces la letra a") # contar


print(texto.swapcase()) # cambiar mayusculas por minisculas y viceversa
print(texto.startswith('Ya'))
print(texto.endswith('C#'))
print(texto.replace('Python', 'Go'))

texto_2 = 'este es un titulo'
print(texto_2)
print(texto_2.capitalize()) 
print(texto_2.title())
print(texto_2.isdigit())
print("12".isdigit())