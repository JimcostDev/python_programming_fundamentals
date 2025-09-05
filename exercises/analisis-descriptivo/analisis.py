from sklearn.model_selection import train_test_split

def explorar_datos(df):
    """
    Imprime información básica y descriptiva del DataFrame.
    """
    print("Primeras filas del dataset:")
    print(df.head())
    print("\nEstadísticas descriptivas:")
    print(df.describe())
    print("\nInformación general:")
    print(df.info())

def verificar_valores_nulos(df):
    """
    Muestra la cantidad de valores nulos por columna.
    """
    print("\nValores nulos por columna:")
    print(df.isnull().sum())

def dividir_datos(df, tamano_prueba=0.3, semilla=42):
    """
    Separa el DataFrame en conjuntos de entrenamiento y validación.
    """
    df_entrenamiento, df_prueba = train_test_split(df, test_size=tamano_prueba, random_state=semilla)
    print(f"\nTamaño del conjunto de entrenamiento: {df_entrenamiento.shape}")
    print(f"Tamaño del conjunto de validación: {df_prueba.shape}")
    return df_entrenamiento, df_prueba

def calcular_correlaciones(df, columna_objetivo='cnt'):
    """
    Calcula y retorna la matriz de correlación (excluyendo 'dteday' si existe).
    """
    if 'dteday' in df.columns:
        df_numerico = df.drop(columns=['dteday'])
    else:
        df_numerico = df.copy()
    matriz_correlacion = df_numerico.corr()
    print(f"\nCorrelación de '{columna_objetivo}' con el resto de variables:")
    print(matriz_correlacion[columna_objetivo].sort_values(ascending=False))
    return matriz_correlacion
