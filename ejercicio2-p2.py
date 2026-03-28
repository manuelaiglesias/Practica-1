playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]


def Duracion_total(playlist):
    # Inicializo acumuladores
    total_minutos = 0
    total_segundos = 0
    # Obtengo los minutos y segundos separados

    for elemento in playlist:
        duracion = elemento["duration"] 
        minutos, segundos = duracion.split(":")
        minutos = int(minutos)
        segundos = int(segundos)

    # Acumulo

        total_minutos += minutos
        total_segundos += segundos

    # Saco los minutos extra

    total_minutos = total_minutos +(total_segundos // 60)
    total_segundos = total_segundos % 60

    return total_minutos, total_segundos

def Cancion_larga (playlist):
    largo = 0
    for elemento in playlist:
        duracion = elemento["duration"] 
        minutos, segundos = duracion.split(":")
        minutos = int(minutos)
        segundos = int(segundos)
        total = (minutos*60) + segundos
        if largo < total:
            largo = total
            nombre =elemento["title"]
    return nombre, largo        

def Cancion_corta (playlist):
    largo = 9999999
    for elemento in playlist:
        duracion = elemento["duration"] 
        minutos, segundos = duracion.split(":")
        minutos = int(minutos)
        segundos = int(segundos)
        total = (minutos*60) + segundos
        if largo > total:
            largo = total
            nombre = elemento["title"]
    return nombre, largo   

#Programa Principal
minutos, segundos = Duracion_total(playlist)
print(f"La duración total es: {minutos}m {segundos}s")

titulo, largo = Cancion_larga(playlist)
print (f"El titulo de la cancion mas larga es {titulo}, con {largo}s")

titulo2, largo2 = Cancion_corta(playlist)
print (f"El titulo de la cancion mas corta es {titulo2}, con {largo2}s")