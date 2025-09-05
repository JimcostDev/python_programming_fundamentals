"""
    Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

    Si el número del año no es divisible entre cuatro, es un año común.
    De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
    De lo contrario, si el número del año no es divisible entre 400, es un año común.
    De lo contrario, es un año bisiesto.
    
    El código debe mostrar uno de los dos mensajes posibles, que son Año bisiesto o Año común, según el valor ingresado.

    Sería bueno verificar si el año ingresado cae en la era gregoriana y emitir una advertencia de lo contrario: 
    No dentro del período del calendario gregoriano. Consejo: utiliza los operadores != y %.
    
    DATOS DE PRUEBA:
    
    Entrada de muestra: 2000

    Resultado esperado: Año bisiesto

    Entrada de muestra: 2015

    Resultado esperado: Año común 

    Entrada de muestra: 1999

    Resultado esperado: Año común 

    Entrada de muestra: 1996

    Resultado esperado: Año bisiesto 

    Entrada de muestra: 1580

    Resultado esperado: No dentro del período del calendario gregoriano
"""
### forma 1
year_ = int(input("Introduzca un año: "))

if (year_ > 1582):
    if (year_ % 4 != 0):
        print('{}, Año común'.format(year_))
    elif (year_ % 100 != 0):
        print('{}, Año bisiesto'.format(year_))
    elif (year_ % 400 != 0):
        print('{}, Año común'.format(year_))
    else:
        print('{}, Año bisiesto'.format(year_))


else:
    print('No esta dentro del período del calendario gregoriano')

### forma 2
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
                
    return leap

year = int(input("Enter a year: "))
print(is_leap(year))

### otra alternativa
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")