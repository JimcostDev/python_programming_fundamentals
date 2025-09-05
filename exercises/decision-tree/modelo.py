from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def dividir_datos(df):
    """
    Separa las variables predictoras (X) y la respuesta (y) y divide
    el dataset en entrenamiento (70%) y prueba (30%).
    """
    X = df.drop(columns=['admit'])
    y = df['admit']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    print("\nDimensiones de los conjuntos:")
    print("Entrenamiento:", X_train.shape, "Prueba:", X_test.shape)
    return X_train, X_test, y_train, y_test

def entrenar_modelo(X_train, y_train):
    """
    Entrena un árbol de decisión con los datos de entrenamiento.
    """
    modelo = DecisionTreeClassifier(random_state=42)
    modelo.fit(X_train, y_train)
    return modelo

def evaluar_modelo(modelo, X_test, y_test):
    """
    Realiza predicciones y muestra métricas de evaluación.
    """
    y_pred = modelo.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    reporte = classification_report(y_test, y_pred)
    
    print("\nExactitud del modelo:", acc)
    print("\nMatriz de confusión:")
    print(cm)
    print("\nReporte de clasificación:")
    print(reporte)
    return y_pred, acc, cm, reporte
