rounds = [
    {
        'theme': 'Entrada', 
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7,'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 8,'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 9,'judge_3': 8},
            'Santiago': {'judge_1': 6, 'judge_2': 7,'judge_3': 6},
            'Lucía': {'judge_1': 8, 'judge_2': 8,'judge_3': 8},
    }
},
   {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9,'judge_3': 8},
            'Mateo': {'judge_1': 8, 'judge_2': 7,'judge_3': 9},
            'Camila': {'judge_1': 7, 'judge_2': 6,'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 8,'judge_3': 8},
            'Lucía': {'judge_1': 7, 'judge_2': 8,'judge_3': 7},
    }
},
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8,'judge_3': 7},
            'Mateo': {'judge_1': 9, 'judge_2': 9,'judge_3': 8},
            'Camila': {'judge_1': 8, 'judge_2': 7,'judge_3': 9},
            'Santiago': {'judge_1': 7, 'judge_2': 7,'judge_3': 6},
            'Lucía': {'judge_1': 9, 'judge_2': 9,'judge_3': 9},
    }
},
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9,'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 6,'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 8,'judge_3': 8},
            'Santiago': {'judge_1': 8, 'judge_2': 9,'judge_3': 7},
            'Lucía': {'judge_1': 7, 'judge_2': 7,'judge_3': 8},
    }
},
{
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8,'judge_3': 9},
            'Mateo': {'judge_1': 8, 'judge_2': 9,'judge_3': 8},
            'Camila': {'judge_1': 7, 'judge_2': 7,'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 9,'judge_3': 9},
            'Lucía': {'judge_1': 8, 'judge_2': 8,'judge_3': 7},
        }
    }
]


# Creo un diccionario para guardal el participante con su total por ronda
dicc = {}
def Calcular (elemento):
    # Recorro los participantes dentro del campo scores
    for participante in elemento["scores"]:
        # Dentro de cada participante acumulo el puntaje de los jueces 
        total = elemento["scores"][participante]["judge_1"]+elemento["scores"][participante]["judge_2"]+elemento["scores"][participante]["judge_3"]
        # Guardo en el dicc 
        dicc[participante]=total
    # Convirto el dicc en tuplas
    dicc.items()
    # Ordeno de mayor a menor 
    ranking = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
    # Devuelvo el ranking y el ganador 
    return ranking[0], ranking


# Imprimo la tabla con el ganador 
def Imprimir(ganador,tabla):
    print(f"NOMBRE  PUNTAJE")
    for nombre, puntaje in tabla:
        print(nombre,puntaje)
    print(f"El ganador de la ronda es: {ganador[0]}, con {ganador[1]} puntos.")
    print(f"-------------------------------------------------------------")
    

# Creo un diccionario para guardar los que ganan rondas
acumulo = {}
def Ganadores(ganador):
    # Si el ganador no esta que lo agregue
    if ganador not in acumulo:
        acumulo[ganador] = 1
    #Si esta que le sume uno 
    else:
        acumulo[ganador] += 1 


# Creo un diccionario para acumular los totales por participantes
tot = {}
def Sumo_puntaje(tabla):
    for (nombre, puntaje) in tabla:
        if nombre not in tot:
            tot[nombre] = puntaje
        else:
            tot[nombre] += puntaje
    return tot             


# Creo un diccionario paraguardar los mejores puntajes de los participantes 
puntaje_mas_alto = {}
def Mejores_puntaje(tabla):
    for (nombre, puntaje) in tabla:
        # Si el participante no está en el diccionario, lo agrego con su puntaje
        if nombre not in puntaje_mas_alto:
            puntaje_mas_alto[nombre] = puntaje
        else:
            # Si ya está, comparo y guardo el mayor
            if puntaje > puntaje_mas_alto[nombre]:
                puntaje_mas_alto[nombre] = puntaje

# Recorro ronda por ronda 
def Programa(rounds):
    for elemento in rounds:
        # Veo en que ronda estamos 
        if elemento["theme"] == "Entrada":
            print(f"Ronda 1 - Entrada")
            # Busco el ganador y la tabla con el calcular
            ganador, tabla = Calcular(elemento)
            # Imprimo la tabla y l ganador
            Imprimir(ganador,tabla)
            # Le paso el nombre del ganador para que contabice las veces que gana 
            Ganadores(ganador[0])
            # Le paso la tabla de puntajes de cada ronda para que acumule 
            Sumo_puntaje(tabla)
            # Guardo los puntajes mas altos
            Mejores_puntaje(tabla)
        elif elemento["theme"] == "Plato principal":
            print(f"Ronda 2 - Plato principal")
            ganador2, tabla2 = Calcular(elemento)
            Imprimir(ganador2,tabla2)
            Ganadores(ganador2[0])
            Sumo_puntaje(tabla2)
            Mejores_puntaje(tabla2)
        elif elemento["theme"] == "Postre":
            print(f"Ronda 3 - Postre")
            ganador3, tabla3 = Calcular(elemento)
            Imprimir(ganador3,tabla3)
            Ganadores(ganador3[0])
            Sumo_puntaje(tabla3)
            Mejores_puntaje(tabla3)
        elif elemento["theme"] == "Cocina internacional":
            print(f"Ronda 4 - Cocina internacional") 
            ganador4, tabla4 = Calcular(elemento)
            Imprimir(ganador4,tabla4)
            Ganadores(ganador4[0])
            Sumo_puntaje(tabla4)
            Mejores_puntaje(tabla4)
        elif elemento["theme"] == "Final libre":
            print(f"Ronda 5 - Final libre")
            ganador5, tabla5 = Calcular(elemento)
            Imprimir(ganador5,tabla5)
            Ganadores(ganador5[0])
            Sumo_puntaje(tabla5)
            Mejores_puntaje(tabla5)
    
    # Imprimo el acumulado, las rondas ganadas y el promedio
    
    print(f"El puntaje acumulado por participantes es {tot}")
    
    print(f"-------------------------------------------------------------")
    
    print(f"Las rondas ganadas por cada participante es: {acumulo}")
    
    print(f"-------------------------------------------------------------")
    print(f"Promedios")
    for participante in tot:
        promedio = tot[participante]/5
        print(f"{participante}:{promedio}")

    print(f"-------------------------------------------------------------")
    print(f"Los meores puntajes de cada participante son: {puntaje_mas_alto}")

# Programa Principal
puntaje= Programa(rounds)

