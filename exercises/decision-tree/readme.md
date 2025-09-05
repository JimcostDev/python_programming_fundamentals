# Proyecto: Árbol de Decisión para Admisiones a Posgrado

## Descripción
Este proyecto utiliza un algoritmo de clasificación basado en árboles de decisión para predecir la variable `admit` en un conjunto de datos de admisiones a estudios de posgrado. Se transforma la variable "Chance of Admit" en una variable categórica (≥ 0.6: `yes`, de lo contrario: `no`). El código está organizado en módulos para mejorar su mantenimiento y escalabilidad.

## Estructura del Proyecto
El proyecto se divide en los siguientes archivos:

- **datos.py**  
  - `cargar_datos(ruta_archivo="Admission_Predict.csv")`: Carga el dataset utilizando `kagglehub` y retorna un DataFrame de pandas.  
  - `preprocesar_datos(df)`: Muestra información inicial, transforma la variable de admisión en categórica y elimina la columna original.

- **modelo.py**  
  - `dividir_datos(df)`: Separa las variables predictoras (X) y la variable respuesta (y), dividiendo el dataset en entrenamiento (70%) y prueba (30%).  
  - `entrenar_modelo(X_train, y_train)`: Entrena un árbol de decisión usando los datos de entrenamiento.  
  - `evaluar_modelo(modelo, X_test, y_test)`: Evalúa el modelo retornando predicciones, exactitud, matriz de confusión y reporte de clasificación.

- **graficos.py**  
  - `graficar_arbol(modelo, columnas)`: Visualiza el árbol de decisión.  
  - `graficar_importancia_caracteristicas(modelo, columnas)`: Genera un gráfico de barras que muestra la importancia de cada característica.  
  - `graficar_matriz_confusion(cm)`: Visualiza la matriz de confusión utilizando un mapa de colores.

- **main.py**  
  - Script principal que orquesta el flujo completo del proyecto: carga y preprocesamiento de datos, división del dataset, entrenamiento del modelo, evaluación y visualización de los resultados.

## Dependencias
El proyecto requiere las siguientes dependencias:

- `kagglehub`
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`

Para instalarlas, puedes ejecutar:
```bash
pip install kagglehub[pandas-datasets] scikit-learn matplotlib pandas numpy
```
O instalar todas las dependencias usando el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```