"""
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. 
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
"""

import requests
import json

def showAllLeagues():
    url = f"https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        print(data)
        print(json.dumps(data, indent=4))
    else:
        print(f"Error al llamar a la API: {response.status_code}")


def searchPlayer(name):
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={name}"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        print(data)
        print(json.dumps(data, indent=4))
    else:
        print(f"Error al llamar a la API: {response.status_code}")

showAllLeagues()
searchPlayer('Messi')