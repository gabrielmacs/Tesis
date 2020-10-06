import spacy
import os
import json
import nltk
from spacy import displacy
from collections import Counter
from nltk import SnowballStemmer




nombreArchivoJSON = "noticias.json"
rutaActualpy = os.path.dirname(os.path.abspath(__file__))
# os.path.dirname(os.path.abspath(__file__)) obtiene la ruta del archivo actual
pathArchivoJSON = os.path.join(rutaActualpy, nombreArchivoJSON)



data = {}
data['noticias'] = []

spanishstemmer = SnowballStemmer("spanish")


#nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("es_core_news_sm")

palabrasClave = ['gobi', 'gobern', 'secretari', 'centr', 'univers', 'escuel', 'institut', 'ministeri',
                 'gobiern', 'alcald', 'republ', 'subsecretari', 'viceministeri', 'director', 'gerent', 'dueñ', 'propietari']

texto = """

Cerca de 100 personas están bajo vigilancia epidemiológica en el país debido al caso sospechoso del nuevo coronavirus (2019-nCoV) que las autoridades del Ministerio de Salud Pública confirmaron ayer, domingo 26 de enero del 2020. Se trata de los pasajeros que compartieron vuelo con el ciudadano chino, de 49 años de edad, que salió desde Hong Kong con destino Quito. “No existe el coronavirus en Ecuador. Estamos investigando un caso sospechoso”, aclaró este lunes 27 de enero de 2020 la ministra de Salud, Catalina Adramuño. Luego de una entrevista en una estación radial en Guayaquil indicó que en 72 horas tendrán los resultados de las pruebas de diagnóstico aplicadas al paciente. Otros análisis han descartado que se trate de influenza u otros virus respiratorios. “El paciente se encuentra asilado en un hospital público, al momento está estable, está orientado en tiempo y espacio”, informó la ministra. Además señaló que hay un familiar del posible afectado, quien también está en seguimiento y no presenta síntomas. El ciudadano chino, originario de Fujian-Fuquing (China), arribó a Ecuador el pasado 21 de enero del 2020. Tres días después presentó tos, expectoración, temperatura de 39°C, dolor torácico y signos de insuficiencia respiratoria y renal. Según la ministra, existe la posibilidad de que el paciente tuviera una comorbilidad o una enfermedad de base.\nAndramuño además aseguró que han reforzado los controles en puertos, aeropuertos y pasos fronterizos del país. En el aeropuerto de Guayaquil, por ejemplo, indicó que laboran tres epidemiólogos. Según la procedencia de los pasajeros, explicó que elaboran una historia clínica, realizan un examen físico y registran los contactos con direcciones domiciliarias para realizar un seguimiento. Este protocolo se aplica a los pasajeros que provienen de los países donde se han reportado casos del 2019-nCoV. En entrevista con Radio América informó además que trabajan con la Dirección General de Aviación Civil para que, de acuerdo a los lineamientos de la Organización Panamericana de la Salud (OPS), la tripulación de las diferentes aeronaves comunique si detecta pasajeros con sintomatología respiratoria a los puestos de vigilancia instalados en las terminales aéreas. China registró los primeros casos a fines de 2019. La Organización Mundial de la Salud (OMS) aún no califica como emergencia internacional el brote del coronavirus de Wuhan, que hasta las 10:15 de este lunes 27 de enero del 2020, el Gobierno de China y la OMS registran 81 muertes y 2 886 contagios a escala mundial. Durante la tarde y noche del domingo 26 de enero, se difundió una noticia falsa cuya imagen 'confirmaba' tres casos del virus en el país. Frente a la serie de rumores que circulan en redes sociales sobre posibles casos del coronavirus de Wuhan en Ecuador, Andramuño solicita a la ciudadanía ecuatoriana mantenerse informada a través de fuentes oficiales. \"La información está en las páginas del Ministerio de Salud Pública. Estaremos dando vocería a escala nacional para que la ciudadanía conozca, sobre todo, para transmitirle que estamos trabajando avalados en los protocolos de la Organización Mundial de la Salud y la Organización Panamericana de la Salud y que no exista pánico\", dijo Andramuño en diálogo con Ecuador TV.\nAsimismo, la ministra anunció que la comunidad ecuatoriana residente en China -que de acuerdo con la Cancillería de Ecuador a son 1 194 ecuatorianos, nueve de ellos residentes en Wuhan- está fuera de peligro y descartó contagios. Las autoridades del MSP recomiendan un lavado constante de manos y el uso de gel antiséptico. Si hay síntomas gripales es aconsejable usar mascarillas, evitar sitios de concurrencia masiva y aplicar medidas al estornudar o toser, como el uso de pañuelo o con el ángulo interno del codo.
"""


doc = nlp(texto)


print("\n\n*****Entidades que pueden ser stakeholders (partes interesadas) AUTORES*****\n")
ubicacionesTemasTotales = []
autoresTotales = Counter(palabra.text+" "+palabra.label_ for palabra in doc.ents if palabra.label_ != 'MISC'and palabra.label_ !=
                         'DATE' and palabra.label_ != 'CARDINAL' and palabra.label_ != 'ORDINAL' and palabra.label_ != 'PERCENT' and palabra.label_ != 'QUANTITY')
for nombre in autoresTotales:
    if(autoresTotales[nombre] > 2):
        ubicacionesTemasTotales.append(nombre)

print("\n\n*****Temas que pueden ser representativos TEMAS*****")

temasTotales = Counter(
    palabra.text for palabra in doc.ents if palabra.label_ == 'MISC')
for nombre in temasTotales:
    if(temasTotales[nombre] > 1):
        print(nombre, temasTotales[nombre])


print("\n\n***** REPETICIONES *****")
nombres = [w.lemma_.lower() for w in nlp(texto)
           if w.is_stop != True and w.is_punct != True and w.pos_ != 'CONJ' and w.pos_ != 'SPACE' and w.pos_ != 'NUM' and w.pos_ != 'ADP' and len(w) > 2]

print("\n\n***** stemming: palabras en raices *****")
autoresStemming = []
raicesPalabras = [spanishstemmer.stem(token) for token in nombres]
for i, rp in enumerate(raicesPalabras):
    for pc in palabrasClave:
        if rp == pc:
            autoresStemming.append(
                nombres[i]+" "+nombres[i+1]+" "+nombres[i+2])

print (autoresStemming)


print("\n\n***** stemming: palabras en raices *****")

frasesDosPalabras = []
frasesTresPalabras = []
i = 0
# se construye arreglo de dos y tres palabras seguidas, aunque para el caso
# de dos palabras, se busca palabras repetidas que esten a la izq o der
while i < len(nombres):
    if(i == len(nombres)-1):
        frasesDosPalabras.append(nombres[i] + " " + nombres[i-1])
        i += 1
    elif(i == len(nombres)-2):
        frasesDosPalabras.append(nombres[i] + " " + nombres[i+1])
        frasesDosPalabras.append(nombres[i] + " " + nombres[i-1])
        i += 1
    elif(i == 0):
        frasesDosPalabras.append(nombres[i] + " " + nombres[i+1])
        i += 1
    else:
        frasesDosPalabras.append(nombres[i] + " " + nombres[i+1])
        frasesDosPalabras.append(nombres[i] + " " + nombres[i-1])
        frasesTresPalabras.append(
            nombres[i] + " " + nombres[i+1]+" " + nombres[i+2])
        i += 1


frasesFrecuenteRepetidas = Counter(frasesDosPalabras).most_common(40)
frasesFrecuente = []
frasesTresPalabrasArreglo = []
frasesDosPalabrasArreglo = []
for i in range(0, len(frasesFrecuenteRepetidas), 2):
    frasesFrecuente.append(frasesFrecuenteRepetidas[i])

print("\n30 palabras más repetidas:")
print(Counter(nombres).most_common(30))
print("\n20 juegos de dos palabras más repetidas:")
print(frasesFrecuente)
for f in frasesFrecuente:
    frasesDosPalabrasArreglo.append(f[0])
print("\n10 juegos de tres palabras más repetidas:")
jurgosTresPalabras = Counter(frasesTresPalabras).most_common(10)
for j in jurgosTresPalabras:
    frasesTresPalabrasArreglo.append(j[0])

print(frasesTresPalabrasArreglo)

data['noticias'].append({
    'Juegos de tres palabras': frasesTresPalabrasArreglo,
    'Juegos de dos palabras': frasesDosPalabrasArreglo,
    'Autores': autoresStemming,
    'Ubicaciones': ubicacionesTemasTotales
})


with open(pathArchivoJSON, 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
