import json
import os
from collections import Counter

from resumen import Resumen

nombreArchivoJSON = "ActoresTemas.json"
rutaActualpy = os.path.dirname(os.path.abspath(__file__))
pathArchivoJSON = os.path.join(rutaActualpy, nombreArchivoJSON)



dataAT = {}
dataAT['Actores y temas'] = []

actoresTotales = []
temasTotales =[] 
palabrasClaveRecibidas=['casa', 'mesa']

with open('dataelcomercio.json',encoding="utf8") as file:
    data = json.load(file)
    resumen=Resumen("ES")
    resumen.procesarPalabrasClave(palabrasClaveRecibidas)
    for i,noticia in enumerate(data['noticias']):
        print(i,"___________________________________________________________________")
        
        if (noticia['text']!=[]):
            resumen.procesarTexto(noticia['text'])
     
        
            actoresTotales.extend(resumen.actoresStemming)

            temasTotales.extend(resumen.frasesDosPalabrasNoRepetidas)
            temasTotales.extend(resumen.frasesTresPalabras)
    

    c1=Counter(temasTotales).most_common(100)


    
    c2=Counter(actoresTotales).most_common(50)
    print(temasTotales)

    dataAT['Actores y temas'].append({
    'Actores': c2,
    'Temas': c1
    })




with open(pathArchivoJSON, 'w',encoding="utf8") as file:
    json.dump(dataAT, file, indent=4, ensure_ascii=False)

"""

   
   print('Actores:', resumen.actoresStemming)
        print('Frases dos palabras:', resumen.frasesDosPalabrasNoRepetidas)
        print('Frases tres palabras:', resumen.frasesTresPalabrasNoRepetidas)
        print("_____")
        resumen.etiquetarPalabras()
        print('Palabras miscelaneas repetidas:', resumen.entMiscEvNacProdObr)
        print('Palabras repetidas:', resumen.etiquetadasTodasNoMisc)






with open('Git/noticias/noticias.json') as file:
    data = json.load(file)
    resumen=Resumen()
    resumen.procesarPalabrasClave("palabrasClave.txt")
    resumen.procesarTexto("Un avión con 201 estadounidenses evacuados de la ciudad de Wuhan (China), epicentro del brote de coronavirus, aterrizó este miércoles 29 de enero del 2020 en una base militar de Riverside, en California. La nave fletada por el Departamento de Estado originalmente estaba programada para aterrizar en el Aeropuerto Internacional de Ontario, a unas 40 millas (64 kilómetros) de Los Ángeles. Sin embargo, la tarde del martes los Centros para el Control y Prevención de Enfermedades anunciaron el nuevo lugar de aterrizaje, más alejado de zonas residenciales. En su trayecto a California, el avión hizo una escala en Anchorage, en Alaska, para reabastecer gasolina, y dónde los pasajeros fueron sometidos a revisiones médicas para poder continuar su viaje hacia California. Los 201 pasajeros, entre los que se encuentran personal del cuerpo diplomático, y una decena de menores, serán sometidos a una nueva revisión en las instalaciones militares de la base March Air Reserve Base, ubicada a unas 65 millas (110 kilómetros) del centro de Los Ángeles. En el área de California ya se reportaron dos casos del brote, mientras en Estados Unidos hay en total cinco casos confirmados por los CDC. Las imágenes aéreas de los medios locales mostraron el avión estacionado en la mitad de la pista con la escalera extendida sin que los pasajeros descendieran inmediatamente. Esta mañana medios nacionales informaron de que la Casa Blanca estudia la posibilidad de imponer una prohibición temporal de los vuelos hacia y desde China debido a la enfermedad, que ha causado ya casi 6 000 contagios confirmados y 132 muertes. El brote de coronavirus en China ha ido empeorando y extendiéndose, ya que además de en EE.UU., se han dado casos aislados en al menos otros 13 países, aunque sin registrase ninguna muerte. Algunas aerolíneas habían suspendido ya gran cantidad de vuelos entre Estados Unidos y China, citando en parte una disminución significativa de la demanda, pero United Airlines y American Airlines han decidido congelar totalmente a partir de febrero algunas de sus rutas con China debido a la propagación del coronavirus. De acuerdo a medios, American Airlines cancelará de momento sus vuelos de Los Ángeles a Shanghái y Pekín del 9 de febrero al 27 de marzo.")
    print('Actores:', resumen.autoresStemming)
    print('Frases dos palabras:', resumen.frasesDosPalabrasNoRepetidas)
    print('Frases tres palabras:', resumen.frasesTresPalabrasNoRepetidas)
"""




"""
quitar verbos de Actores
obtener pesos de cada palabra y sumar al numero de veces repetidas sumar valor de wiki, google noticias y academico(numero de veces que sale en google)

preguntar: obtener un autor y un tema de todas las noticias 
como es la integracio  al conectar con Graphql
"""
"""
diccionario de archivo texto 
enriquesiendo diccionario segun las noticias
mandar al correo


si me sale como auto, que no me salga como tema
corregir organizacion panarica y salud publica que no salga en tema 



redactar dos cosasplaneap
def

1teprica de lo que estamos hciedno 
1.1descripcion de librerias y tecnicas que stamos usando 
1.2con referencias
1.3que es normalizar steemin raices, etc
s
doac bdd
si se necesita el numero de veces que se repite"""