#Ejercicio: Escribe un programa que solicite al usuario una lista de números 
# y luego muestre el promedio de esos números.

lista_numeros=input("Introduce una lista de números: ")
numeros=lista_numeros.split()
numero_numeros=len(numeros)
for i in range(0,numero_numeros): #convierto una list[str] en una list[float]. Si uso una list[int] no funciona para decimales
    numeros[i]=float(numeros[i])
suma=sum(numeros)
promedio=suma/numero_numeros
print("El promedio de la lista", numeros, "es:", promedio)