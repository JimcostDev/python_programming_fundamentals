from paquetes import * # Importa todos los módulos que se encuentran en __all__
from paquetes import VERSION

print(f"Versión: {VERSION}")
modulo1.saludar('Ronaldo')
modulo2.saludar('Paula')


# otra forma de importar
import paquetes.modulo1 as m1
m1.saludar('JimcostDev')