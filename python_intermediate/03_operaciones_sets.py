"""
NOTA: No se pueden realizar operaciones con otras colecciones de datos, solo se puede únicamente entre conjuntos.
"""

set_a = {'col', 'mex', 'esp'}
set_b = {'arg', 'col'}

print("UNIÓN")
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)
print()

print("INTERSECCIÓN")
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)
print()

print("DIFERENCIA")
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)
print()

print("DIFERENCIA SYMETRICA")
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)