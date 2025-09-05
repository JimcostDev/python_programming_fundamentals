# En una casa de cambio necesitan construir un programa tal que dado como dato una cantidad
# expresada en dólares, convierta esa cantidad a pesos. Además, debe proyectar la equivalencia en
# pesos de ese valor para los próximos 7 días, si se sabe que el valor esta aumentando un 3% cada
# día.

valor_dolar_en_pesos = 4043.28
tasa_aumento = 0.03

# funcion para convertir de dolares a pesos
def convertir_dolares_a_pesos(dolar):
    pesos = dolar*valor_dolar_en_pesos
    return pesos

# función que calcula el valor aumentado al 3% los proximos 7 dias
def calcular_valor_proximos_7dias(dolar):
    valores_lista = []
    for dia in range(7):
        precio = dolar + (dolar*tasa_aumento)
        precio = round(precio, 2)
        valores_lista.append(precio) # añado a la lista
        dolar = valores_lista[dia] # tomar el valor del dia siguiente
    return valores_lista


# EJECUCIÓN DEL PROGRAMA
dolar_in = float(input('Digite la cantidad en dolares: '))
pesos = convertir_dolares_a_pesos(dolar_in)
print(pesos)
aumento_7dias = calcular_valor_proximos_7dias(pesos)
print(aumento_7dias)