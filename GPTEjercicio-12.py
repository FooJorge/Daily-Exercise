#Ejercicio: Crea un arreglo de numpy con 10 números aleatorios. 
#Luego, encuentra los índices del valor mínimo y máximo en el arreglo.

import numpy as np

numeros = np.random.randint(0, 100, 10) # Crea un arreglo de numpy con 10 números aleatorios entre 0 y 100

# Encontrar el valor mínimo, máximo y promedio de los números en el arreglo
minimo = np.min(numeros)
indice_minimo=np.argmin(numeros)
maximo = np.max(numeros)
indice_maximo=np.argmax(numeros)

# Mostrar los resultados
#print(numeros) #Por si quiero ver la lista de números para comprobar que es correcto
print("El valor mínimo es:", minimo, "cuyo índice es el arreglo es:", indice_minimo)
print("El valor máximo es:", maximo, "cuyo índice es el arreglo es:", indice_maximo)
