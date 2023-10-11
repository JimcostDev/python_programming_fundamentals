# mis variables
nota_trabajos = []
nota_parcial = 0.0


#contador = 1
for x in range(1, 3):
    nota = float(input(f'Ingrese nota trabajo {x} => '))
    nota_trabajos.append(nota)
    #contador +=1

nota_final_trabajos = sum(nota_trabajos)/2
#print(nota_final_trabajos)

nota_parcial = float(input(f'Ingrese nota parcial => '))
nota_final = (nota_final_trabajos * 0.6) + (nota_parcial * 0.4)

if nota_final >= 6:
    print(f'Aprobo con {nota_final}')
else:
    print(f'Repobro con {nota_final}')