# EJEMPLO 1
ingredientes = ['🐔', '🐮', '🥔', '🍇']

mapeo_ingredientes = {
    '🐔': '🍗',
    '🐮': '🍔',
    '🥔': '🍟',
    '🍇': '🍷'
}

# Usamos map para aplicar el mapeo de ingredientes a cada elemento de la lista
resultado = list(map(lambda x: mapeo_ingredientes.get(x, '🍪'), ingredientes))

print(resultado)

# EJEMPLO 2
items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

# impuestos
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items)
