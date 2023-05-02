#Ejercicio: Escribe un programa que solicite al usuario una lista de números
# y luego muestre los números que son mayores que 5.

lista_numeros=input("Introduce una lista de números: ")
numeros=lista_numeros.split()
numeros=[float(i) for i in numeros]
mayores_cinco=[]

for i in numeros:
    if i > 5.0:
       mayores_cinco.append(i) #append(x) añade el elemnto x al final de la lista

print("Los números mayores que 5 son: ", mayores_cinco)