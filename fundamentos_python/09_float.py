# compración de numeros tipo float
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y) 
print()

# transformación de y a string 
y_str = format(y, ".2g")
print(y_str)
print('str =>', y_str)
#print(type(y_str))
#print(type(x))
print(y_str == str(x))
print()

# # tolerancia
print(x)
print(y)
tolerancia = 0.00001
r = x - y # 3.3 - 3.300000003
print(abs(r)) # valor absoluto
print(abs(r) < tolerancia)
print()

#round 
y_round = round(y,2)
print(x)
print(y_round)
print(x == y_round)