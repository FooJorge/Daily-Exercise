#Ejercicio: Escribe un programa que solicite al usuario una frase y luego muestre la
# frase con las palabras en orden inverso.

frase=input("Introduce una frase: ")
palabras=frase.split()
palabras_invertida=palabras[::-1]
frase_invertida= " ".join(palabras_invertida)
print("La frase invertida es:", frase_invertida)