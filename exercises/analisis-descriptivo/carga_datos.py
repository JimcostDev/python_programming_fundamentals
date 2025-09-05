import pandas as pd
from ucimlrepo import fetch_ucirepo
# dataframe es una estructura de datos bidimensional, similar a una tabla de base de datos
def cargar_datos_bicicletas():
    """
    Carga el conjunto de datos de uso compartido de bicicletas desde ucimlrepo y lo devuelve como un DataFrame.
    """
    dataset = fetch_ucirepo(id=275) # Bike Sharing Dataset
    caracteristicas = dataset.data.features
    objetivo = dataset.data.targets
    df = pd.concat([caracteristicas, objetivo], axis=1) # Concatenar características y objetivo
    return df
