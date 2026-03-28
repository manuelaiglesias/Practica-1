
# Calculo precio

def Calculo(peso,zona):
    if zona == "local":
        if peso < 1:
            costo = 500
        elif 1 <= peso < 5:
            costo = 1000
        else:
            costo = 2000
    elif zona == "regional":
        if peso < 1:
            costo = 1000
        elif 1 <= peso < 5:
            costo = 2500
        else:
            costo = 5000
    elif zona == "nacional":
        if peso < 1:
            costo = 2000
        elif 1 <= peso < 5:
            costo = 4500
        else:
            costo = 8000
    else:
        return None      
    return costo        


# Programa Principal
peso = float(input(f"Ingrese el peso del paquete: "))
zona = input(f"Ingrese la zona destino(local/regional/nacional): ").lower()

costo_envio = Calculo(peso,zona)
if costo_envio is None:
    print("Zona no válida.")
else:
    print(f"Costo de envío: {costo_envio}")