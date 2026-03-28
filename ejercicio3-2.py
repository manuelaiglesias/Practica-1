review = """La película sigue a un grupo de astronautas que 
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo 
a través
de tormentas solares y fallos en el sistema de navegación. Al 
llegar
a Marte descubren que la base está abandonada y los 
suministros
destruidos. Torres decide sacrificar la nave nodriza para 
salvar
al equipo y logran volver a la Tierra en una cápsula de 
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje 
secreto."""

# Pido que ingrese los spoilers y los pongo todos e minuscla
spoiler = input(f"Ingrese las palabras spoiler (separadas por coma)").lower()

# Transformo la los string en una lista sepatrada por comas
lista = spoiler.split(",")

# Paso revew a minuscula
texto = review.lower()

# Recorro la lista y pregunto porcada palabra si aparece en el texto, si es asi que transforme en *
for palabra in lista:
    if palabra in texto:
        texto = texto.replace(palabra, "*" * len(palabra))

# Imprimo el nuevo texto
print(texto)


