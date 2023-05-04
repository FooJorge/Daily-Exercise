#Ejercicio: Crea un arreglo de numpy con 20 números aleatorios. 
# Luego, crea una nueva matriz que contenga solo los números impares 
#del arreglo original.

import numpy as np

numeros=np.random.randint(0,100,20)

numeros_impares=[]

for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        numeros_impares.append(numeros[i])

#print(numeros)
print("Los números impares son:")
print(numeros_impares)