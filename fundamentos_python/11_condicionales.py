if True:
  print('deberia ejecutarse')

if False:
  print('nunca se ejecuta')


team = input('cual es tu equipo favorito de la premier? ')

if team == 'liverpool':
  print('Sos de los "Reds"')
elif team == 'city':
  print('Sos de los "Citizens"')
elif team == 'arsenal':
  print('Sos de los "Gunners"')
else:
  print('no tienes ninguna equipo interesante')

champions = int(input('¿Cuantas champions tiene tu club? => '))

if champions >= 2: 
  print('¡Son buenos eh!')
else:
  print('Estan mejorando')

