print (f"Tabla psiciones| Toeneo de futbol | ")

def Mostrar menu ():
    print (f"Menu del torneo ")
    print (f" 1. Agregar equipo")
    print (f " 2. Guardar resultados ")
    print (f" 3. Mostrar tabla de posiciones ")
    print (f" 4. Salir ")

tabla ={}

def Agregar equipo (nombre):
    if nombre not in tabla:
        tabla[nombre]={
            "pj":0, "pg":0, "pp":0
            "gf":0, "gc":0, "puntos":0
        }
        print(f "Equipo {nombre} fue agregado a la tabla ")
    else:
        print (f" El equpo ya estaba registrado ")    

def Actualizar resultados (equipo1, equipo2, gole1, gole2)
    tabla[equipo1] [pj] += 1
    tabla [equipo2] [pj]+=1
    if gole1 > gole2:
        tabla [equipo1][pg]+=1
        tabla [equipo1][gf]+=gole1
        tabla [equipo1][gc]+=gole2
        tabla [equipo1][puntos]+=3
        tabla [equipo2][pp]+=1
        tabla [equipo2][gf]+=gole2
        tabla [equipo2][gc]+=gole1
    elif gole1 < gole2:
        tabla [equipo2][pg]+=1
        tabla [equipo2][gf]+=gole2
        tabla [equipo2][gc]+=gole1
        tabla [equipo2][puntos]+=3
        tabla [equipo1][pp]+=1
        tabla [equipo1][gf]+=gole1
        tabla [equipo1][gc]+=gole2
    else gole1 = gole2:
        tabla [equipo2][gf]+=gole2
        tabla [equipo2][gc]+=gole1
        tabla [equipo1][gf]+=gole1
        tabla [equipo1][gc]+=gole2

def Eliminar equipo (nombre)

