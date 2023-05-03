#Ejercicio: Crea un DataFrame de pandas con información sobre algunos países. 
#Incluye las columnas "País", "Población" y "PIB per cápita". 
#Luego, encuentra el país con el mayor PIB per cápita.

import pandas as pd

dict1={'Pais':['Portugal','España', 'Italia', 'Francia'],
             'Poblacion': [10.35, 47.62, 60.24, 67.75],
             'PIB': [20870, 25500, 35675, 36660]}

informacion=pd.DataFrame(dict1)


print("El País con mayor PIB per cápita es:")
print(informacion[informacion.PIB==informacion.PIB.max()])