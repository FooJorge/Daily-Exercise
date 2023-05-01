#Ejercicio: Escribe un programa que solicite al usuario una frase y 
#luego muestre la cantidad de veces que aparece cada palabra en la frase.

frase=input("Introduce una frase: ")
palabras=frase.split() #type list
numero_palabras=len(palabras)
for i in range(0,numero_palabras):
    print(palabras[i],"=",palabras.count(palabras[i]))