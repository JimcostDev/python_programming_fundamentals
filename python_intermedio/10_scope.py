price = 100 # global

def increment():
  price = 200 # local
  result = price + 10
  return result

print(price)
price_2 = increment()
print(price_2)
# print(result)