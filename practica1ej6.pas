{
Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
finalizar.  
}
multiplos= []
no_multiplos= []
N= int(input("ingrese un numero"))
i=1
for i in range(1,N):
    if i%5==0:
        multiplos.append(i)
    else:
        no_multiplos.append(i)  
print("multiplos de 5", multiplos)
print("no multiplos de", no_multiplos)         
        
