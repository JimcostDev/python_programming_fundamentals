from app import ideal_weight as iw

# Llamamos a la función que devuelve el IMC, clasificación y estatura
imc, clasificacion, estatura = iw.IMC()

# Mostramos los resultados y la clasificación
print(iw.mostar_resultados_imc(imc, clasificacion))

# Mostramos el peso normal para la estatura
print(iw.mostrar_peso_normal(estatura))  