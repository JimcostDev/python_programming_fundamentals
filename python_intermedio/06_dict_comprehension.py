# {key:value for var in iterable}

# ejemplo 1
dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict)

dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)
print()

# ejemplo 2
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)
print()

"""
dict comprehension condicional
"""
# {key:value for var in iterable if condition}
# ejemplo 3
teams = ['liverpool', 'arsenal', 'chelsea', 'spurs']
fans= { team: random.randint(1, 100)  for team in teams}
print(fans)
result = {team: fans for (team, fans) in fans.items() if fans > 30}
print(result)
print()

text = 'Hola, soy Ronaldo'
unique = { c: text.count(c) for c in text if c in 'aeiou' }
print(unique)