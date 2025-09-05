from datos import cargar_datos, preprocesar_datos
from modelo import dividir_datos, entrenar_modelo, evaluar_modelo
from graficos import graficar_arbol, graficar_importancia_caracteristicas, graficar_matriz_confusion

def main():
    # 1. Cargar y preprocesar datos
    df = cargar_datos()
    df = preprocesar_datos(df)
    
    # 2. Dividir el conjunto de datos
    X_train, X_test, y_train, y_test = dividir_datos(df)
    
    # 3. Entrenar el modelo
    modelo = entrenar_modelo(X_train, y_train)
    
    # 4. Evaluar el modelo
    y_pred, acc, cm, reporte = evaluar_modelo(modelo, X_test, y_test)
    print("\nPredicciones:")
    print(y_pred)
    print("\nReporte de clasificación:")
    print(reporte)
    print("\nExactitud del modelo:", acc)
    print("\nMatriz de confusión:")
    print(cm)
    
    # 5. Graficar resultados
    graficar_arbol(modelo, X_train.columns)
    graficar_importancia_caracteristicas(modelo, X_train.columns)  
    graficar_matriz_confusion(cm)  

if __name__ == '__main__':
    main()
