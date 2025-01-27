# El Índice de Masa Corporal (IMC) es una medida que relaciona el peso y
# la estatura de una persona para estimar si tiene un peso adecuado.
# Se calcula con la fórmula:
# IMC = peso (kg) / estatura^2 (m)

# Rango de IMC (clasificación según la OMS):
# - Bajo peso: IMC < 18.5
# - Normal: IMC 18.5–24.9
# - Sobrepeso: IMC 25–29.9
# - Obesidad: IMC >= 30 (Obesidad tipo I: 30–34.9, Obesidad tipo II: 35–39.9, Obesidad tipo III: >= 40)

# Calcula el Índice de Masa Corporal (IMC) de una persona
def calcular_imc(peso: float, estatura: float) -> float:
    return peso / estatura ** 2

# Clasifica el IMC según la OMS
def clasificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad tipo I"
    elif imc < 40:
        return "Obesidad tipo II"
    else:
        return "Obesidad tipo III"
    
# Calcular peso maximo dentro del rango de IMC normal
def calcular_peso_maximo(estatura: float) -> float:
    return 24.9 * estatura ** 2

# Calcular peso minimo dentro del rango de IMC normal
def calcular_peso_minimo(estatura: float) -> float:
    return 18.5 * estatura ** 2

# Mostar peso maximo y minimo dentro del rango de IMC normal
def mostrar_peso_normal(estatura: float) -> str:
    peso_minimo = calcular_peso_minimo(estatura)
    peso_maximo = calcular_peso_maximo(estatura)
    return f"El peso normal para una estatura de {estatura} m debe estar entre {peso_minimo:.2f} y {peso_maximo:.2f} kg"


# Mostrar resultados del IMC
def mostar_resultados_imc(imc: float, clasificacion: str) -> str:
    return f"El IMC es {imc:.2f} y se clasifica como {clasificacion}"

def IMC():
    peso = float(input("Ingrese el peso en kg (por ejemplo, 70.3): "))
    estatura = float(input("Ingrese la estatura en metros (por ejemplo, 1.84): "))
    
    # Calcular IMC y clasificarlo
    imc = calcular_imc(peso, estatura)
    clasificacion = clasificar_imc(imc)
    
    # Devolver los resultados para que se usen en main.py
    return imc, clasificacion, estatura