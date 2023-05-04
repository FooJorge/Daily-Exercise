#Ejercicio: Crea un DataFrame de pandas con información sobre algunos países. 
#Incluye las columnas "País", "Población" y "Área". 
#Luego, calcula la densidad de población para cada país y agrega 
#una nueva columna al DataFrame.

import pandas as pd

dict1={'Pais':['Portugal','España', 'Italia', 'Francia'],
    'Poblacion': [10.35, 47.62, 60.24, 67.75],
    'Area':[92230, 505990, 302340, 643800]}

df=pd.DataFrame(dict1)

df['Densidad']=(df.Poblacion/df.Area)*1000000

print(df)
