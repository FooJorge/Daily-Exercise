# Ejercicio: Escribe un programa que solicite al usuario una frase y luego muestre la
# cantidad de palabras que contiene.

frase=input('Escribe una frase: ')
espacios=frase.count(' ')
palabras=espacios+1 #Una frase contiene una palabra más que el número de espacios que tiene
print("La frase:", frase, "contiene", palabras, 'palabras')
