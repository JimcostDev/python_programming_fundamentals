import matplotlib.pyplot as plt
import seaborn as sns

def configurar_graficos():
    """
    Configura estilos y temas para los gráficos.
    """
    plt.style.use('ggplot')
    sns.set_theme(style='whitegrid')

def graficar_matriz_correlacion(matriz_correlacion):
    """
    Visualiza la matriz de correlación.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    plt.show()

def graficar_distribucion(df, columna='cnt'):
    """
    Grafica la distribución de la variable especificada.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[columna], bins=30, kde=True)
    plt.title(f"Distribución de '{columna}'")
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

def graficar_dispersion(df, columna_x='temp', columna_y='cnt'):
    """
    Grafica un gráfico de dispersión entre dos variables.
    """
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x=columna_x, y=columna_y)
    plt.title(f"Relación entre {columna_x} y {columna_y}")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.tight_layout()
    plt.show()

def graficar_caja(df, columna_x='season', columna_y='cnt'):
    """
    Grafica un diagrama de caja para ver la distribución de 'cnt' por 'season'.
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x=columna_x, y=columna_y)
    plt.title(f"Distribución de {columna_y} por {columna_x}")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.tight_layout()
    plt.show()
