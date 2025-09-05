# Proyecto de Análisis Descriptivo de Datos

Este proyecto realiza un análisis descriptivo del conjunto de datos de uso compartido de bicicletas (*Bike Sharing Dataset*). El objetivo es explorar y visualizar los datos para obtener información relevante sobre el uso de bicicletas en diferentes condiciones.

## Estructura del Proyecto

El proyecto está organizado en los siguientes módulos:

- **carga_datos.py**: Contiene la función para cargar y preparar el conjunto de datos.
- **analisis.py**: Incluye funciones para explorar y analizar los datos.
- **graficos.py**: Proporciona funciones para la visualización gráfica de los datos.
- **main.py**: Script principal que orquesta la ejecución de los módulos anteriores.

## Requisitos

**Crear y activar el entorno virtual:**

   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install pandas matplotlib seaborn scikit-learn ucimlrepo
```
Alternativamente, se pueden instalar todas las dependencias con:

```bash
pip install -r requirements.txt
```

--- 
### Descripción de las Funciones por Módulo

1. `carga_datos.py`
- `cargar_datos_bicicletas()`: Esta función carga el conjunto de datos de uso compartido de bicicletas desde la biblioteca ucimlrepo y lo devuelve como un DataFrame de pandas.
  
2. `analisis.py`
- `explorar_datos(df)`: Imprime las primeras filas, estadísticas descriptivas e información general del DataFrame proporcionado, ayudando a comprender la estructura y características básicas de los datos.

- `verificar_valores_nulos(df)`: Muestra la cantidad de valores nulos por columna en el DataFrame, facilitando la identificación de datos faltantes.

- `dividir_datos(df, tamano_prueba=0.3, semilla=42)`: Separa el DataFrame en conjuntos de entrenamiento y prueba según el tamaño de prueba especificado (por defecto, 30%) y la semilla para la reproducibilidad.

- `calcular_correlaciones(df, columna_objetivo='cnt')`: Calcula y retorna la matriz de correlación del DataFrame, excluyendo la columna 'dteday' si está presente. Además, imprime la correlación de la columna objetivo especificada con las demás variables.

3. `graficos.py`
- configurar_graficos(): Configura los estilos y temas predeterminados para los gráficos utilizando las bibliotecas matplotlib y seaborn.

- `graficar_matriz_correlacion(matriz_correlacion)`: Genera y muestra un mapa de calor que visualiza la matriz de correlación proporcionada, facilitando la identificación de relaciones entre variables.

- `graficar_distribucion(df, columna='cnt')`: Crea un histograma con una curva de densidad para mostrar la distribución de la variable especificada del DataFrame.

- `graficar_dispersion(df, columna_x='temp', columna_y='cnt')`: Genera un gráfico de dispersión para visualizar la relación entre dos variables especificadas del DataFrame.

- `graficar_caja(df, columna_x='season', columna_y='cnt')`: Crea un diagrama de caja (boxplot) que muestra la distribución de la variable 'cnt' en función de las categorías de 'season', permitiendo comparar la variabilidad y distribución entre diferentes estaciones.

Estas funciones, cuando se integran en el script principal main.py, permiten realizar un análisis descriptivo completo del conjunto de datos, desde la carga y exploración inicial hasta el análisis estadístico y la visualización gráfica de los resultados.