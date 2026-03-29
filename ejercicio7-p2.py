# Pido los participantes
nombres = input(f"Ingrese los participantes (separados por comas): ").lower()

# Lo convierto en una lista
lista = nombres.split(",")

import random

# Veo si hay tres
if len(lista) >= 3:
    # Uso el set para eliminar si hay duplicados y comparar
    if len(lista) != len(set(lista)):
        print("Hay nombres duplicados")
    else:  
        # Mezclo 
        random.shuffle(lista)
        # Creo la lista 2 mezclada
        lista2 = lista[1:] + lista[:1]
        # Asigno de amigos, emparejo dos listas con el zip
        print(f"Sorteo:")
        for participante, amigo in zip(lista, lista2):
            print(f"{participante} → {amigo}")
else:
    print(f"Debe haber mas participantes.")
