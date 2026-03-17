{
Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
del 1 al 10 utilizando un bucle for. 
}

numero= int(input("ingrese el numero para conocer su tabla de multiplicar"))
i=1
for i in range (1,11):
    print(f"{numero} por {i} = {numero*i}")
