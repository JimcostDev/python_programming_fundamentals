# dependencias a instalar:
# pip install pandas matplotlib seaborn scikit-learn ucimlrepo

# alternativamente, se pueden instalar todas las dependencias con:
# pip install -r requirements.txt

from carga_datos import cargar_datos_bicicletas
from analisis import explorar_datos, verificar_valores_nulos, calcular_correlaciones
from graficos import configurar_graficos, graficar_matriz_correlacion, graficar_distribucion, graficar_dispersion, graficar_caja

def main():
    # Configurar estilos de gráficos
    configurar_graficos()

    # Cargar datos
    df = cargar_datos_bicicletas()

    # Exploración inicial
    explorar_datos(df)
    verificar_valores_nulos(df)
    
    # Análisis de correlaciones y visualización
    matriz_correlacion = calcular_correlaciones(df, columna_objetivo='cnt')
    graficar_matriz_correlacion(matriz_correlacion)

    # Visualizaciones adicionales
    graficar_distribucion(df, columna='cnt')
    graficar_dispersion(df, columna_x='temp', columna_y='cnt')
    graficar_caja(df, columna_x='season', columna_y='cnt')

if __name__ == "__main__":
    main()
