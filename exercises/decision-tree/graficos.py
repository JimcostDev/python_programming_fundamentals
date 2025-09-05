import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import numpy as np

def graficar_arbol(modelo, columnas):
    """
    Visualiza el árbol de decisión.
    """
    plt.figure(figsize=(18,8))
    plot_tree(modelo, feature_names=columnas, class_names=['no', 'yes'], filled=True)
    plt.title("Árbol de Decisión")
    plt.show()

def graficar_importancia_caracteristicas(modelo, columnas):
    """
    Muestra un gráfico de barras con la importancia de cada característica.
    """
    importancias = modelo.feature_importances_
    indices = np.argsort(importancias)
    plt.figure(figsize=(10,6))
    plt.barh(range(len(importancias)), importancias[indices], color='skyblue')
    plt.yticks(range(len(importancias)), [columnas[i] for i in indices])
    plt.xlabel("Importancia")
    plt.title("Importancia de las Características")
    plt.show()

def graficar_matriz_confusion(cm):
    """
    Visualiza la matriz de confusión usando un mapa de colores.
    """
    plt.figure(figsize=(6,6))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title("Matriz de Confusión")
    plt.colorbar()
    tick_marks = np.arange(2)
    plt.xticks(tick_marks, ['no', 'yes'], rotation=45)
    plt.yticks(tick_marks, ['no', 'yes'])
    
    # Añadir los números en cada celda
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                     ha="center", va="center",
                     color="white" if cm[i, j] > thresh else "black")
    
    plt.ylabel('Etiqueta Verdadera')
    plt.xlabel('Etiqueta Predicha')
    plt.tight_layout()
    plt.show()
