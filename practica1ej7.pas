{
 Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
espacios. Las palabras cortas deben ser excluidas del resultado final.
}
lista_nueva=[]
entrada = input("Ingrese palabras separadas por comas: ")
lista_palabras = entrada.split(",")   
for palabra in lista_palabras:
    if len(palabra)>3:
        lista_nueva.append(palabra)
oracion = " ".join(lista_nueva)
print("La oración final es:", oracion)
