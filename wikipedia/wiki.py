#https://wikipedia.readthedocs.io/en/latest/code.html#api
#wikipedia.suggest( consulta ) 
#Obtenga una sugerencia de búsqueda de Wikipedia para consultas . Devuelve una cadena o Ninguno si no se encontró ninguna sugerencia.
#wikipedia.summary( consulta , oraciones = 0 , caracteres = 0 , auto_suggest = True , redirect = True ) 
#wikipedia.geosearch( latitud , longitud , título = Ninguno , resultados = 10 , radio = 1000 )

import wikipedia
wikipedia.set_lang("es")
print("RESUMEN******************")
print(wikipedia.summary("Ciudad de México"))
print("SUGERENCIA******************")
print(wikipedia.suggest("Ciudad de México"))
print("BUSQUEDA******************")
print(wikipedia.search("Ciudad de México"))
