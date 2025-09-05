
"""
iter() nos permite controlar la forma en que se ejecutar un iterador, esto nos ayuda a no ocupar tanta memoria
"""
for i in range(1, 10):
  print(i)

my_iter = iter(range(1, 4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))