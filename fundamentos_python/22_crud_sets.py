paises = {'col', 'mex', 'esp'}
size = len(paises)

print(size)
print('col' in paises)
print('arg' in paises)

# add
paises.add('bra')
print(paises)
paises.add('bra')
print(paises)

# update
paises.update({'col', 'arg', 'esp'})
print(paises)

# remove
paises.remove('mex')
print(paises)
paises.discard('ale')
print(paises)

# clear
paises.clear()
print(paises)