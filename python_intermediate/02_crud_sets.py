set_countries = {'col', 'mex', 'esp'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('per' in set_countries)

# add
set_countries.add('bra')
print(set_countries)
set_countries.add('bra')
print(set_countries)

# update
set_countries.update({'arg', 'ecu', 'bra'})
print(set_countries)

# remove
set_countries.remove('col')
print(set_countries)

# discard(): Elimina un elemento y si este no existe no lanza ningún error.
# remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
set_countries.remove('ar')
set_countries.discard('ar')
print(set_countries)

# limpiar todo el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))