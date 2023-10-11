def switch_case(case):
    switcher = {
        'opcion1': 'Has seleccionado la opción 1',
        'opcion2': 'Has seleccionado la opción 2',
        'opcion3': 'Has seleccionado la opción 3'
    }
    return switcher.get(case, 'Opción inválida')

# Ejemplo de uso
opcion = 'opcion2'
resultado = switch_case(opcion)
print(resultado)