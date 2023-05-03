#Ejercicio: Crea un DataFrame de pandas con información sobre algunas películas. 
#Incluye las columnas "Título", "Año", "Duración" y "Director". 
#Luego, encuentra las películas con una duración mayor a 120 minutos.

import pandas as pd

dict1={'Pelicula': ['Nomadland', 'Parasitos', 'Green Book', 'La forma del agua', 'Moonlight', 'Spotlight'],
       'Año': [2021, 2020, 2018, 2017, 2016, 2015],
       'Duracion': [108, 132, 130, 123, 111, 128],
       'Director': ['Chloé Zhao', 'Bong Joon-ho', 'Peter Farrelly', 'Guillermo Del Toro', 'Barry Jenkins', 'Tom McCarthy']}

peliculas=pd.DataFrame(dict1)

peliculas_duracion=peliculas[peliculas['Duracion']>120]

print("Las películas que duran más de 120 minutos son:")
print(peliculas_duracion)