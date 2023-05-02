#Ejercicio: Escribe un programa que solicite al usuario una lista de números
#  y luego muestre el número más grande y el más pequeño de la lista.

lista_numeros=input("Introduce una lista de números: ")
numeros=lista_numeros.split()
numero_numeros=len(numeros)
for i in range(0,numero_numeros): #convierto una list[str] en una list[float]. Si uso una list[int] no funciona para decimales
    numeros[i]=float(numeros[i])
minimo=min(numeros)
maximo=max(numeros)
print("De la lista, el número más grande es {} y el número más pequeño {}".format(maximo, minimo))