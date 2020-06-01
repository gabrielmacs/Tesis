import json
from Resumen import Resumen



with open('Git/noticias/noticias.json') as file:
    data = json.load(file)
    resumen=Resumen()
    resumen.procesarPalabrasClave("palabrasClave.txt")
    for i,noticia in enumerate(data['noticias']):
        print(i,"___________________________________________________________________")
        print(noticia['Titulo'])
        resumen.procesarTexto(noticia['Texto'])
        print('Autores:', resumen.autoresStemming)
        print('Frases dos palabras:', resumen.frasesDosPalabrasNoRepetidas)
        print('Frases tres palabras:', resumen.frasesTresPalabrasNoRepetidas)


"""
quitar verbos de autores
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