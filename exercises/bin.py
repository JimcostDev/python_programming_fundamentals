import math
import json

# mis variables
numero = 10.5;
print("El número es: ", numero);
parte_fraccionaria, parte_entera = math.modf(numero);
num_decimal = int(parte_entera); 


# estas variables son para calcular la parte en fraccion
dobles = [];
dobles.append(parte_fraccionaria);
lista_fracciones = []; #claves
lista_binaria = []; #valores
diccionario_resultados = {}

# función que convirte de decimal a binario la parte en fraccion
def convertirABinarioParteFraccionaria():
    for i in range(64):
        valor = dobles[i] * 2;
        dobles.append(valor);
        # separo los decimales de las partes enteras
        p_fraccion, p_entera = math.modf(dobles[i]);
        p_fraccion = round(p_fraccion,2); # redondeo el numero a 2 decimales
        lista_fracciones.append(p_fraccion);
        frac, ent = math.modf(lista_fracciones[i]);
        lista_binaria.append(frac*2);
        if(lista_binaria[i] == 1.0):
            break;

    #lleno la lista(resulatdo) con cada parte entera para formar el binario(b)
    resultado = []
    for b in lista_binaria:
        resultado.append(int(b)); #aqui solo me quedo con la parte entera

    #convertir lista a str
    cadena = str(resultado);
    numero_sin_comas = cadena.replace(',', '');
    numero_sin_espacios = numero_sin_comas.replace(' ', '');
    return numero_sin_espacios

# función que convierte de binario a decimal
def binarioADecimal(binario):
    bi_de = int(binario);
    return bi_de;

#función que convierte decimal a binario
def decimalABinario(decimal):
    de_bi = bin(decimal);
    return de_bi;



resultado_decimal_bin = decimalABinario(num_decimal)
print(f'El numero decimal: {num_decimal} a binario es = {resultado_decimal_bin[2:]}');
print(f'su parte fraccionaria en binario es = {convertirABinarioParteFraccionaria()}');
print()

# partes dobles 
print('PARTES DOBLES, PASO A PASO: #KEYS')
print(lista_fracciones);

print("""
CON ESTA LISTA FORMO EL BINARIO DE LA PARTE EN FRACCION: #VALUES """);
print(lista_binaria);

print("""
VER RESULTADOS: """);
for idx, valor in enumerate(zip(lista_fracciones,lista_binaria)):
    diccionario_resultados[idx] = valor;
print(json.dumps(diccionario_resultados, indent=2))

"""
descomentar el codigo de abajo si queremos mostar la conversion de binario a decimal (solo partes enteras), 
siempre inicia con 0b y despues va el binario
"""
# num_binario = 0b111101; # aqui colocamos un numero binario si queremos convertirlo a decimal
# print(f'El numero binario: {bin(num_binario)} a decimal es = {binarioADecimal(num_binario)}');



