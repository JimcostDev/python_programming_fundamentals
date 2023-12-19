a = 23
b = 34
if a == 34 or b == 34:
    print(f'{a + b} = or')

a = 23
b = 30
if a == 23 and b == 30:
    print(f'{a + b} = and')


object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')