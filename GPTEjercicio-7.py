#Ejercicio: Escribe un programa que solicite al usuario una frase y 
#luego muestre la cantidad de veces que aparece cada palabra en la frase.

frase = input("Introduce una frase: ")
palabras = frase.split()
frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(palabra, "-", frecuencia)
