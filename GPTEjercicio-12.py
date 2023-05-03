#Ejercicio: Crea un arreglo de numpy con 10 números aleatorios. 
#Luego, encuentra los índices del valor mínimo y máximo en el arreglo.

import numpy as np

numeros = np.random.randint(0, 100, 10) # Crea un arreglo de numpy con 10 números aleatorios entre 0 y 100

# Encontrar el valor mínimo, máximo y promedio de los números en el arreglo
minimo = np.min(numeros)
indice_minimo=np.where(numeros==minimo)
maximo = np.max(numeros)
indice_maximo=np.where(numeros==maximo)

# Mostrar los resultados
print(numeros) #Por si quiero ver la lista de números para comprobar que es correcto
print("El valor mínimo es:", minimo, "cuyo índice es el arreglo es:", indice_minimo[0]) #indice_minimo devuelve una tupla de dos valores, el que nos interesa es el primero [0]
print("El valor máximo es:", maximo, "cuyo índice es el arreglo es:", indice_maximo[0])