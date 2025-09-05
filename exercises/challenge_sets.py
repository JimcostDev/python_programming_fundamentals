"""
Para resolver este desafío, debes escribir un algoritmo que elimine los elementos 
repetidos para obtener un conjunto único llamado champions.

Este algoritmo recibirá como entrada cuatro conjuntos de equipos, 
estos equipos serán de toda europa.
"""

teams = {"LIVERPOOL", "BAYER MUNICH", "ARSENAL", "JUVENTUS"}
italy = {"MILAN", "JUVENTUS"}
england = {"LIVERPOOL", "ARSENAL", "MANCHESTER UNITED"}
spain = {"REAL MADRID", "BARCELONA", "VALENCIA"}

# Escribe tu solución 👇
champions = teams.union(italy,england,spain)
print(champions)