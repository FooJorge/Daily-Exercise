# Ejercicio: Escribe un programa que solicite al usuario una frase y luego muestre la
# cantidad de palabras que contiene.

frase = input("Introduce una frase: ")
cantidad_palabras = len(frase.split()) #la función split divide la frase en palabras y la función len cuenta el número de palabras 

print("La frase:", frase, "tiene", cantidad_palabras, "palabras.")
