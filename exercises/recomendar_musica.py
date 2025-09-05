# Crear una función  que reciba cómo parámetro un género musical, 
#la cual te recomiende escuchar una canción de dicho género musical.

# Parametro (genero)
#1. Rock
#2. Electronica
#3. Musica clasica
#4. Balada
#5. Salsa
#6. Bachata

#datos adicional --cancion recomendada

# funcion que recomienda una canción por genero musical y artista
def recomendar_cacion_por_genero(genero):
    artista=input(f'Escribe el nombre del artista musical del genero {genero}: ')
    artista=artista.lower()
    if genero== 'rock':   
        musica= recomendar_musica(artista)
        return musica 
    
    elif genero=='electronica':
        musica= recomendar_musica(artista)
        return musica
    
    elif genero=='musica clasica':
        musica= recomendar_musica(artista)
        return musica
    
    elif genero=='balada':
        musica= recomendar_musica(artista)
        return musica
    
    elif genero=='salsa':
        musica= recomendar_musica(artista)
        return musica
    
    elif genero=='bachata':
        musica= recomendar_musica(artista)
        return musica
    else:
        return 'No te puedo recomendar mas canciones'

# funcion que recomienda una canción de acuerdo al artista
def recomendar_musica(artista):
    if artista== 'mana':
            return 'Labios compartidos'
    elif artista=='miguel bose':
            return'Si tu no vuelves'
    elif artista=='andrea bocelli':
            return 'con te partiro'
    elif artista=='jose jose':
            return 'El triste'
    elif artista=='david guetta':
            return 'Turn me on - David guetta ft Nicky Minaj'
    elif artista=='grupo chaney':
            return 'Amor de Privamera'
    elif artista=='prince royce':
            return 'Darte un beso'
    else:
            return 'No te puedo recomendar mas canciones'

# EJECUCIÓN 
genero=input('Dime un genero musical: ')
genero=genero.lower()
resultado=recomendar_cacion_por_genero(genero)
print(resultado)


    
