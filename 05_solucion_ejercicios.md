# SOLUCIÓN DE EJERCICIOS
## 1. Calcular el área de un triángulo:
```python
Inicio
  # Declaración de variables
  Real base, altura, area

  # Entrada de datos
  Leer base
  Leer altura

  # Cálculo del área
  area = (base * altura) / 2

  # Salida de resultados
  Escribir "El área del triángulo es:", area
Fin
```
## 2. Convertir grados Celsius a Fahrenheit:
```python
Inicio
  # Declaración de variables
  Real celsius, fahrenheit

  # Entrada de datos
  Leer celsius

  # Conversión de grados Celsius a Fahrenheit
  fahrenheit = (celsius * 9/5) + 32

  # Salida de resultados
  Escribir "La temperatura en grados Fahrenheit es:", fahrenheit
Fin
```

## 3. Calcular el promedio de tres números:
```python
Inicio
  # Declaración de variables
  Real num1, num2, num3, promedio

  # Entrada de datos
  Leer num1
  Leer num2
  Leer num3

  # Cálculo del promedio
  promedio = (num1 + num2 + num3) / 3

  # Salida de resultados
  Escribir "El promedio de los tres números es:", promedio
Fin
```

## 4. Determinar si un número es par o impar:
```python
Inicio
  # Declaración de variables
  Entero numero

  # Entrada de datos
  Leer numero

  # Verificar si el número es par o impar
  Si (numero % 2 == 0) Entonces
    Escribir "El número es par"
  Sino
    Escribir "El número es impar"
  Fin Si
Fin
```

## 5. Determinar si un número es positivo, negativo o cero:
```python
Inicio
  # Declaración de variables
  Entero numero

  # Entrada de datos
  Leer numero

  # Verificar si el número es positivo, negativo o cero
  Si (numero > 0) Entonces
    Escribir "El número es positivo"
  Sino Si (numero == 0) Entonces
    Escribir "El número es cero"
  Sino
    Escribir "El número es negativo"
  Fin Si
Fin
```

## 6. Determinar si un estudiante aprobó o reprobó una materia (ten en cuenta que los trabajos equivalen al 60% de la nota final y el parcial el 40%):
```python
Inicio
  # Declaración de variables
  Real nota_trabajos
  Real nota_parcial
  Real nota_final

  # Entrada de datos
  Escribir "Ingrese la nota de los trabajos:"
  Leer nota_trabajos

  Escribir "Ingrese la nota del parcial:"
  Leer nota_parcial

  # Cálculo de la nota final
  nota_final = (nota_trabajos * 0.6) + (nota_parcial * 0.4)

  # Verificar si el estudiante aprobó o reprobó
  Si (nota_final >= 6.0) Entonces
    Escribir "El estudiante aprobó la materia."
  Sino
    Escribir "El estudiante reprobó la materia."
  Fin Si
Fin
```

## 7. Determinar si una persona puede votar en base a su edad y nacionalidad:
```python
Inicio
  # Declaración de variables
  Entero edad
  Cadena nacionalidad

  # Entrada de datos
  Escribir "Ingrese la edad de la persona:"
  Leer edad

  Escribir "Ingrese la nacionalidad de la persona:"
  Leer nacionalidad

  # Verificar si la persona puede votar
  Si (edad >= 18) Entonces
    Si (nacionalidad == "Colombiana") Entonces
      Escribir "La persona puede votar."
    Sino
      Escribir "La persona no puede votar debido a su nacionalidad."
    Fin Si
  Sino
    Escribir "La persona no puede votar debido a su edad."
  Fin Si
Fin
```

## 8. Determinar el número mayor dado 3 números:
```python
Inicio
  # Declaración de variables
  Entero num_1
  Entero num_2
  Entero num_3

  # Entrada de datos
  Escribir "Ingrese el número 1:"
  Leer num_1

  Escribir "Ingrese el número 2:"
  Leer num_2

  Escribir "Ingrese el número 3:"
  Leer num_3

  # Verificar el número más grande
  Si (num_1 >= num_2 y num_1 >= num_3) Entonces
    Escribir "El número más grande es:", num_1
  Sino Si (num_2 >= num_1 y num_2 >= num_3) Entonces
    Escribir "El número más grande es:", num_2
  Sino
    Escribir "El número más grande es:", num_3
  Fin Si
Fin
```

## 9. Crear un algoritmo que simule las operaciones básicas de una calculadora (switch y case)
```python
Inicio
  # Declaración de variables
  Real resultado
  Real num1
  Real num2
  Caracter operacion

  # Entrada de datos
  Escribir "Ingrese el primer número:"
  Leer num1

  Escribir "Ingrese el segundo número:"
  Leer num2

  Escribir "Ingrese la operación deseada (+, -, *, /):"
  Leer operacion

  # Realizar la operación según la opción seleccionada
  switch (operacion)
  {
    case "+":
      resultado = num1 + num2
      Escribir "El resultado de la suma es:", resultado
      Romper
      
    case "-":
      resultado = num1 - num2
      Escribir "El resultado de la resta es:", resultado
      Romper
      
    case "*":
      resultado = num1 * num2
      Escribir "El resultado de la multiplicación es:", resultado
      Romper
      
    case "/":
      Si (num2 != 0) Entonces
        resultado = num1 / num2
        Escribir "El resultado de la división es:", resultado
      Sino
        Escribir "Error: No se puede dividir entre cero."
      Fin Si
      Romper
      
    default:
      Escribir "Error: Operación no válida."
  }
Fin
```

## 10. Imprimir los números del 1 al 10.
```python
Inicio
  Entero contador

  Para contador desde 1 hasta 10 hacer
    Escribir contador
  Fin Para
Fin
```

## 11. Imprimir la tabla de multiplicar de un número dado.
```python
Inicio
  # Declaración de variables
  Entero numero

  # Entrada de datos
  Escribir "Ingrese el número para generar la tabla de multiplicar:"
  Leer numero

  # Generar tabla de multiplicar
  Para multiplicador desde 1 hasta 10 hacer
    resultado = numero * multiplicador
    Escribir numero, "x", multiplicador, "=", resultado
  Fin Para
Fin
```
