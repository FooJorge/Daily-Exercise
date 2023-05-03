#Ejercicio: Crea un DataFrame de pandas con información sobre algunas películas.
#Incluye las columnas "Título", "Año", "Duración" y "Director".
#Luego, encuentra el director con más películas en la lista.

import pandas as pd
import numpy as np

dict1={'Pelicula': ['Nomadland', 'Parasitos', 'Green Book', 'La forma del agua', 'Moonlight', 'Spotlight'],
       'Año': [2021, 2020, 2018, 2017, 2016, 2015],
       'Duracion': [108, 132, 130, 123, 111, 128],
       'Director': ['Chloé Zhao', 'Bong Joon-ho', 'Peter Farrelly', 'Guillermo Del Toro', 'Barry Jenkins', 'Tom McCarthy']}

peliculas=pd.DataFrame(dict1)
frecuencia_director={}
directores_peliculas=peliculas['Director']
directores_peliculas=np.reshape(directores_peliculas,len(directores_peliculas))

for director in directores_peliculas:
    if director in frecuencia_director:
        frecuencia_director[director] += 1
    else:
        frecuencia_director[director] = 1

df_frecuencia_director=pd.DataFrame.from_dict(frecuencia_director, orient='index', columns=['Frecuencia']) #Convierte el diccionario en un dataframe
df_frecuencia_director = df_frecuencia_director.sort_values('Frecuencia', ascending=False) #Ordenamos el dataframe por la columna de frecuencia de mayor a menor
director_con_mas_pelis = df_frecuencia_director.index[0] #se selecciona el primer elemento de la columna

print("El director con más películas es:", director_con_mas_pelis)