def es_primo(n):
    """
    Verifica si un número es primo de manera eficiente.
    Args:
        n: Número a verificar
    Returns:
        bool: True si es primo, False si no lo es
    """
    # Los números menores o iguales a 1 no son primos
    if n <= 1:
        return False
    
    # 2 y 3 son números primos
    if n <= 3:
        return True
    
    # Si es divisible por 2 o 3, no es primo
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Verificamos divisibilidad solo hasta la raíz cuadrada del número
    # Incrementando en pasos de 6 para optimizar (todos los primos > 3 son de la forma 6k±1)
    for i in range(5, int(n ** 0.5) + 1, 6):
        # Verificamos si es divisible por i o i+2
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True

def generar_numeros_perfectos(cantidad):
    """
    Genera una cantidad específica de números perfectos utilizando primos de Mersenne.
    Los números perfectos pares se pueden expresar como 2^(p-1) * (2^p - 1), donde
    (2^p - 1) es un número primo conocido como primo de Mersenne.
    Args:
        cantidad: Cantidad de números perfectos a generar
    Returns:
        list: Lista con los números perfectos encontrados
    """
    perfectos = []
    exponente = 2  # Comenzamos con p=2 ya que es el primer primo
    
    while len(perfectos) < cantidad:
        # Calculamos el número de Mersenne: 2^p - 1
        mersenne = 2 ** exponente - 1
        
        # Si el número de Mersenne es primo
        if es_primo(mersenne):
            # Calculamos el número perfecto: 2^(p-1) * (2^p - 1)
            perfecto = 2 ** (exponente - 1) * mersenne
            perfectos.append(perfecto)
            
        exponente += 1
        
    return perfectos

def run():
        """
        Función principal para ejecutar el programa.
        Solicita una cantidad de números perfectos al usuario y los encuentra.
        """
        try:
            cantidad = int(input('Ingrese la cantidad de números perfectos que desea encontrar: '))
            if cantidad <= 0:
                print("Por favor ingrese un número positivo.")
                return
                
            print("\nCalculando números perfectos...")
            lista_perfectos = generar_numeros_perfectos(cantidad)
            
            print("\nNúmeros perfectos encontrados:")
            for i, num in enumerate(lista_perfectos, 1):
                print(f"{i}. {num}")
            print(f'\nTotal: {len(lista_perfectos)} números perfectos.')
            
        except ValueError:
            print("Por favor ingrese un número válido.")

if __name__ == '__main__':
    run()
