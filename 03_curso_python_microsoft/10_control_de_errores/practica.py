loaded_config = """# ¡Archivo de configuración de Rocket Ship!
tanque_de_combustible=4
tanque_de_oxigeno=3
nivel_propulsion_inicial=84
$ Fin del archivo"""

parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        print(f'No se puede analizar: {line}')
print(parsed_config)