# higher other function = funciones de orden superior - hof

# funcion normal
def increment(x):
  return x + 1

# hof
def high_ord_func(x, func):
  return x + func(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1) = 5
print(result)

""" ---------------------------------------------------- """
# función lambda
increment_v2 = lambda x: x + 1
high_ord_func_v2 = lambda x, func: x + func(x)
result = high_ord_func_v2(2, increment_v2)
print(result)

result = high_ord_func_v2(2, lambda x: x + 2)
print(result)

# change
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)