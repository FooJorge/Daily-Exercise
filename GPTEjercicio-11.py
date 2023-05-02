#Ejercicio: Crea un arreglo de numpy con 10 números aleatorios. 
#Luego, encuentra el valor mínimo, máximo y promedio de los números en el arreglo.

import numpy as np

numeros = np.random.randint(0, 100, 10) # Crea un arreglo de numpy con 10 números aleatorios entre 0 y 100

# Encontrar el valor mínimo, máximo y promedio de los números en el arreglo
minimo = np.min(numeros)
maximo = np.max(numeros)
promedio = np.mean(numeros)

# Mostrar los resultados
print("El valor mínimo es:", minimo)
print("El valor máximo es:", maximo)
print("El promedio es:", promedio)