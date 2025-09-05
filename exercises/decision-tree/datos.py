import kagglehub
from kagglehub import KaggleDatasetAdapter
import numpy as np

def cargar_datos(ruta_archivo="Admission_Predict.csv"):
    """
    Carga el dataset usando kagglehub.
    """
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "mohansacharya/graduate-admissions",
        ruta_archivo,
    )
    return df

def preprocesar_datos(df):
    """
    Muestra información inicial, crea la variable categórica 'admit'
    y elimina la columna original de probabilidad.
    """
    print("Primeras 5 filas del dataset:")
    print(df.head())
    
    # Crear variable 'admit' (≥ 0.6 -> 'yes', de lo contrario 'no')
    df['admit'] = np.where(df['Chance of Admit '] >= 0.6, 'yes', 'no')
    df = df.drop(columns=['Chance of Admit '])
    
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    print("\nEstadísticas descriptivas:")
    print(df.describe())
    return df
