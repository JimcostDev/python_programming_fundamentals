# ===============================
# DERIVACIÓN DE FUNCIONES EN PYTHON
# Usando SymPy
# ===============================

from sympy import symbols, diff, sin, cos, ln, exp, Function

# Definimos la variable simbólica
x = symbols('x')

# ===============================
# 1. FUNCIÓN POLINÓMICA
# f(x) = x^n
# ===============================
n = 5
f = x**n
derivada = diff(f, x)
print("Derivada de x^{}: {}".format(n, derivada))  

# ===============================
# 2. FUNCIÓN EXPONENCIAL
# f(x) = a^x
# ===============================
a = 3
f = a**x
derivada = diff(f, x)
print("Derivada de {}^x: {}".format(a, derivada)) 

# f(x) = e^x
f = exp(x)
derivada = diff(f, x)
print("Derivada de e^x: {}".format(derivada))  

# ===============================
# 3. FUNCIÓN LOGARÍTMICA
# f(x) = ln(x)
# ===============================
f = ln(x)
derivada = diff(f, x)
print("Derivada de ln(x): {}".format(derivada))  

# ===============================
# 4. FUNCIONES TRIGONOMÉTRICAS
# f(x) = cos(x), sen(x)
# ===============================
f = cos(x)
derivada = diff(f, x)
print("Derivada de cos(x): {}".format(derivada))  

f = sin(x)
derivada = diff(f, x)
print("Derivada de sen(x): {}".format(derivada))  

# ===============================
# 5. PRODUCTO DE FUNCIONES
# f(x) = g(x) * h(x)
# ===============================
g = Function('g')(x)
h = Function('h')(x)
f = g * h
derivada = diff(f, x)
print("Derivada del producto g(x)·h(x): {}".format(derivada))  

# ===============================
# 6. COCIENTE DE FUNCIONES
# f(x) = g(x) / h(x)
# ===============================
f = g / h
derivada = diff(f, x)
print("Derivada del cociente g(x)/h(x): {}".format(derivada)) 
