"""
def func(args):
    return val

# lambda
func = lambda args: val
"""

# función normal
def incrementar(x):
  return x + 1

result = incrementar(10)
print(result)

# función lambda
increment = lambda x: x + 1

result = increment (20)
print(result)

# otro ejemplo
full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
text = full_name('ronaldo', 'jiménez acosta')
print(text)