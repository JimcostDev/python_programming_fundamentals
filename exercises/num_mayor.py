"""
find the largest number given 3 numbres
"""
num_1 = int(input('type number 1: '));
num_2 = int(input('type number 2: '));
num_3 = int(input('type number 3: '));

if num_1 >= num_2 and num_1 >= num_3:
    print(f'the largest number is: {num_1}')
elif num_2 >= num_1 and num_2 >= num_3:
    print(f'the largest number is: {num_2}')
elif num_3 >= num_1 and num_3 >= num_2:
    print(f'the largest number is: {num_3}')
