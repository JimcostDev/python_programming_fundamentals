with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  # escribir nuevas cosas en el archivo
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')

  # nota:
  # r+ = leer y escribir
  # w+ = reescribe y agrega nuevas lineas