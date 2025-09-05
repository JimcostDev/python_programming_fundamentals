"""
En Python, match es una palabra clave introducida en la versión 3.10 
que forma parte de las expresiones de coincidencia de patrones. 
Esta característica proporciona una forma concisa y elegante de 
comparar valores y ejecutar código basado en esos resultados.
"""
def evaluar_puntaje(puntaje):
  match puntaje:
    case 100:
      print("¡Excelente!")
    case 90 | 80:
      print("Muy bien.")
    case _:
      if puntaje >= 70:
        print("Aprobado.")
      else:
        print("Reprobado.")

evaluar_puntaje(80)  # Imprimirá: Muy bien.

# Python (match)
def describe_dia(dia):
  match dia:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
      print("Día laboral")
    case "sábado" | "domingo":
      print("Fin de semana")
    case _:
      print("Día inválido")

describe_dia("sábado")  # Imprimirá: Día laboral

# # Java (switch-case)
# public void describeDia(String dia) {
#   switch (dia) {
#     case "lunes":
#     case "martes":
#     case "miércoles":
#     case "jueves":
#     case "viernes":
#       System.out.println("Día laboral");
#       break;
#     case "sábado":
#     case "domingo":
#       System.out.println("Fin de semana");
#       break;
#     default:
#       System.out.println("Día inválido");
#   }
# }