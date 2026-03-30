students = [
{"name": "  Ana García ", "grade": "8", "status":
"aprobado"},
{"name": "pedro lópez", "grade": "4", "status":
"DESAPROBADO"},
{"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":
"Aprobado"},
{"name": "ana garcía", "grade": "9", "status":
"aprobado"},
{"name": None, "grade": "7", "status": "aprobado"},
{"name": "Luis Martínez  ", "grade": None, "status":
"aprobado"},
{"name": " carlos RUIZ", "grade": "6", "status":
"aprobado"},
{"name": "PEDRO LÓPEZ ", "grade": "3", "status":
"desaprobado"},
{"name": "  ", "grade": "5", "status": "aprobado"},
{"name": "María Fernández", "grade": "7", "status":
"APROBADO"},
{"name": "Sofía Torres", "grade": "9", "status":
"Aprobado"},
{"name": "  sofía torres ", "grade": "8", "status":
"aprobado"},
{"name": "Carlos Ruiz", "grade": "6", "status":
"APROBADO"},
{"name": "Roberto Díaz", "grade": "absent", "status":
"ausente"},
{"name": "roberto díaz", "grade": "", "status":
"Ausente"},
{"name": None, "grade": None, "status": None},
{"name": "Laura Méndez", "grade": "7", "status":
"aprobado"},
{"name": "  laura méndez", "grade": "8", "status":
"Aprobado"},
{"name": "GABRIELA RÍOS", "grade": "5", "status":
"aprobado"},
{"name": "gabriela ríos ", "grade": "4", "status":
"Desaprobado"},
]
# Creo una nueva para guardar los que cumplen 
limpio = []
def Eliminar_vacio(students):
    # Recorro la lista
    for elemento in students:
        nombre =elemento["name"]
        nota = elemento["grade"]
        # Veo si nombre no esta vacio
        if nombre is not None and nombre.strip() != "":
            # Veo si nota no esta vacia
            if nota is not None and nota.isdigit(): #devuelve true o false si hay un numero
                limpio.append(elemento)
    return(limpio)

def Normalizar_nombres(lista):
    # Recorro la lista y uso title para poner en mayuscula
    for elemento in lista:
        elemento["name"]= elemento["name"].strip().title()
        elemento["status"]= elemento["status"].title()
    return lista    

# Creo un diccionario para que sea mas facil de comparar
dicc = {}
def Duplicados(lista2):
    for elemento in lista2:
        nombre = elemento["name"]
        nota = int(elemento["grade"])
        # Si el nombre no esta que lo agregue
        if nombre not in dicc:
            dicc[nombre] = elemento
        # Si esta que compare y se quede con el mayor
        else:
            if int(dicc[nombre]["grade"]) < nota:
                dicc[nombre] = elemento
    return list(dicc.values())

def Ordnar_alfabeticamente(lista3):
    # Ordena 
    lista3.sort(key=lambda x: x["name"])
    return lista3
# Programa Prnincipal 

lista = Eliminar_vacio(students)
lista2 = Normalizar_nombres(lista)
lista3 = Duplicados(lista2)
lista4 = Ordnar_alfabeticamente(lista3)
print("Nombre Nota Estado")
print("------------------------------------------")
for r in lista4:
    print(r["name"], r["grade"], r["status"])
print("Total de alumnos válidos:", len(lista4))
