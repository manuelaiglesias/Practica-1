import random
# Modificacion 3
words = {
    "programacion": ["python","programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "verduras": ["lechuga", "zanahoria", "tomate", "repollo", "zapallo"],
    "animales":["perro", "gato", "caballo", "vaca", "oveja" ]
}
#

print("¡Bienvenido al Ahorcado!")
print()
# Modificacion 4
cantidad = int(input("Elija la cantidad de rondas que quiere jugar "))
print (f"Las categorias disponibles son: ",",".join(words.keys()))
categoria = input("Elegi una categoria ")
lista_aux = random.sample(words[categoria], (len(words[categoria])))
for i in range (0, cantidad):
    guessed = []
    attempts = 6
# Modificacion 2
    puntos = 0 
#
  # Modificacion 3
    if categoria in words:
        # Modificacion 4
        word = lista_aux.pop()
    #     

        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                print("¡Ganaste!")
        # Modificacion 2 
                puntos +=6
        #                  
                break
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
            
            letter = input("Ingresá una letra: ")
        # Modificacion 1
            if len(letter) != 1 or not letter.isalpha():
                print(f"Entrada no valida")
                continue
        #         
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")
        # Modificacion 2
                puntos -=1
        #                 
            print()
        else:
            print(f"¡Perdiste! La palabra era: {word}")
        # Modificacion 2
            puntos = 0
        print(f"El puntaje es {puntos}")   
    # Modificacion 3    
    else: 
        print("La categoria no existe")
    #     