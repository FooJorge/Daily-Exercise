#Ejercicio: Escribe un programa que solicite al usuario una frase y 
#luego muestre la cantidad de veces que aparece cada palabra en la frase.

frase = input("Introduce una frase: ")
palabras = frase.split() #separo la frase en una lista de palabras
frecuencia_palabras = {} #creo un diccionario vacío. Estructura de un diccionario {'clave1':valor1, 'clave2': valor2,...}

for palabra in palabras: #si la palabra está en el diccionario sumo uno, si no, añado solo la palabra
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items(): #item() de vuelve una lista de tuplas formada por los pares (clave,valor)
    print(palabra, "-", frecuencia)
