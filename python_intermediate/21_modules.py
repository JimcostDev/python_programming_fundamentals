"""
MODULO
Un módulo se puede definir como una biblioteca de código en Python. 
Es una forma de organizar y reutilizar código en programas Python. 
Un módulo generalmente contiene funciones, clases y variables relacionadas 
con un propósito específico. Los módulos permiten dividir el código en archivos 
separados para facilitar la mantenibilidad y la modularidad de un programa. 
Para usar un módulo en un programa, puedes importarlo con la declaración import.
"""
import sys # del sistema
print(sys.version_info)

import re # expresiones regulares
text = 'Mi numero de telefono es 321 123 1021, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)

import time # horas y fechas
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections # para trabajar con listas
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers) # saber la frecuencia de un numero
print(counter)