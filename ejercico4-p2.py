# Ingreso un email
correo = input(f"Igrese un email: ")

# Veo si tiene un @
if correo.count("@") == 1: 
    # Separo el email en dos partes segun el @
    partes = correo.split("@")
    if len(partes) == 2:
        # Verifico que haya un caractr con el len
        if len(partes[0]) > 0:
            if "." in partes[1]:
                # Veo que ni la primera o ultima posicion no sea "@" o "."
                if correo[0] != "@" and correo[0] != "." and correo[-1] != "@" and correo[-1] != ".":
                    # Separo la parte despues del @ con el punto
                    ultimo = partes[1].split(".")
                    if len(ultimo[-1]) >1:
                        print(f"El email es valido.")
                    else:
                        print(f"El email no es valido.")   
                else:
                    print(f"El email no es valido.")   
            else:
              print(f"El email no es valido.")   
        else: 
            print(f"El email no es valido.")
    else:
        print(f"El email no es valido.")
else:
    print(f"El email no es valido.")    
