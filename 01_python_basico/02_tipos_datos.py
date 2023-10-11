# algoritmo que nos muestra que tipo de dato captura una variable.

# variable para almacenar diferetes tipos de datos
variable = 8
tipo_dato = type(variable).__name__

if tipo_dato == 'int':
    print('la variable es un número de tipo: entero')
elif tipo_dato == 'float':
    print('la variable es un número de tipo: float')
elif tipo_dato == 'str':
    print('la variable es de tipo: cadena')
elif tipo_dato == 'bool':
    print('la variable es de tipo: booleana')
elif tipo_dato == 'list':
    print('la variable es de tipo: lista')
elif tipo_dato == 'dict':
    print('la variable es de tipo: diccionario')
