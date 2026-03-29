posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

# Creo dic para tener las palabras con # y cuantas veces aparecen 
hashtag ={}

# Recorro post
for elemento in posts:
    #Separo 
    oracion = elemento.split(" ")
    for palabras in oracion:
        # Pregunto si arrancan con #
        if palabras.startswith("#"):
            # Veo si ya estan 
            if palabras in hashtag:
                hashtag[palabras]= hashtag[palabras]+1
            else:
                hashtag[palabras]=1 

# Creo un lista para guardar los que aparecen mas de una vez
lista =[]
contador = 0
# Recorro el dicc
for elemento in hashtag:
    contador +=1   
    # Veo si aparece mas de una vez
    if hashtag[elemento] > 1:
        # Agrego a la lista 
        lista.append((elemento, hashtag[elemento]))  

print(f"Los hashtags trending (más de una aparición) son: {lista}")
print(f"Total de hashtags unicos: {contador}")
