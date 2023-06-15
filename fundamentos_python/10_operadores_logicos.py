# and
print('AND') # multiplicacion
print('True and True =>', True and True) # 1
print('True and False =>', True and False) # 0
print('False and True =>', False and True) # 0
print('False and False =>', False and False) # 0

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(stock >= 100 and stock <= 1000)
print()

# or
print('OR') # suma
print('True or True =>', True or True) # 1
print('True or False =>', True or False) # 1
print('False or True =>', False or True) # 1
print('False or False =>', False or False) # 0

role = input('Digita el rol => ')
print(role == 'admin' or role == 'vendedor')
print()

# not
print(not True)
print(not False)

print('NOT AND') # inversor
print('not True and True =>', not (True and True)) # 0
print('not True and False =>', not (True and False)) # 1
print('not False and True =>', not (False and True))  # 1
print('not False and False =>', not (False and False))  # 1

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))