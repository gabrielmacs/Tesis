# https://medium.com/@yeralway1/primeros-pasos-en-nlp-con-spacy-un-vistazo-general-734686843a57

import spacy
from spacy import displacy
from collections import Counter

#nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("es_core_news_sm")

texto = """

Autoridades sanitarias de México reportaron este viernes 28 de febrero del 2020 el tercer caso del nuevo coronavirus, al confirmar un nuevo infectado en la capital, que también dio positivo a las pruebas de laboratorio luego de viajar a Italia. “Hasta este momento tenemos tres casos confirmados del nuevo coronavirus. Probablemente los tres se contagiaron de una misma fuente. Los tres son casos importados”, dijo José Luis Alomía, director general de epidemiología de México, en una conferencia de prensa. Horas antes, el Gobierno de Sinaloa, estado del noroeste de México, confirmó el segundo caso de coronavirus en el país, tras realizarle una segunda prueba a un paciente que estuvo también en Italia con el hombre de Ciudad de México que fue el primer contagio conocido en el territorio. \"En Culiacán (capital del estado) hay un caso confirmado de Covid-19, se han seguido todos los protocolos de contención y no debería de pasar a mayores. Estemos pendientes\", escribió en Twitter el gobernador Quirino Ordaz tras una reunión con la Secretaría de Salud estatal. El paciente de 41 años, originario del céntrico estado de Hidalgo, voló desde Ciudad de México a Culiacán, donde estuvo aislado en un hotel en el que se realizaban las dos pruebas confirmatorias. En la misma red social, el secretario de Salud del estado, Efrén Encinas, afirmó tener \"todo contenido y aislado\" en coordinación con la Secretaría de Salud federal y estar preparado para \"atender cualquier caso\". \"A cuidarnos. Seguimos con un caso de Covid-19 confirmado en Sinaloa, pero bien atendido y sin peligro de más contagios\", publicó el funcionario estatal. Horas antes, cuando el caso apenas era sospechoso, el también médico había ofrecido una rueda de prensa en la que explicó que el paciente padecía una sintomatología leve, con un poco de fiebre y dolor de cabeza. Precisó que este caso está relacionado con el caso positivo que se dio en Ciudad de México porque ambas personas estuvieron días antes en un congreso en el norte de Italia, al asegurar que esta persona estaba en Culiacán para dar una conferencia relacionada con su trabajo. Durante la conferencia matutina del presidente de México, Andrés Manuel López Obrador, las autoridades federales confirmaron este viernes el primer caso de coronavirus del país, el segundo detectado en América Latina después del reportado en Brasil. Hugo López-Gatell, subsecretario de Prevención y Promoción de la Salud, señaló que el positivo pertenece a un hombre de 35 años que está hospitalizado en el Instituto Nacional de Enfermedades Respiratorias (INER). Los dos primeros casos están relacionados con un mexicano residente en Bérgamo, en el norte de Italia, lugar donde se produjeron los contagios en la tercera semana de febrero. Aunque los funcionarios de salud han pedido evitar el pánico, recomiendan a la población lavarse las manos de manera constante, tapar su boca al toser o estornudar, evitar tocarse la cara y no saludar de abrazo o de beso a las personas desconocidas. También han alertado por noticias falsas que se difunden por redes sociales, por lo que exhortan a solo hacer caso a fuentes oficiales.

"""


doc = nlp(texto)




print("\n\n*****Entidades que pueden ser stakeholders (partes interesadas) AUTORES*****\n")

autoresTotales=Counter(palabra.text+" "+palabra.label_ for palabra in doc.ents if palabra.label_!='MISC'and palabra.label_!='DATE' and palabra.label_!='CARDINAL' and palabra.label_!='ORDINAL' and palabra.label_!='PERCENT' and palabra.label_!='QUANTITY'  )
for nombre in autoresTotales:
  if(autoresTotales[nombre] > 2): 
    print (nombre,autoresTotales[nombre])

print("\n\n*****Temas que pueden ser representativos TEMAS*****")

temasTotales=Counter(palabra.text for palabra in doc.ents if palabra.label_=='MISC')
for nombre in temasTotales:
  if(temasTotales[nombre] > 1): 
    print (nombre,temasTotales[nombre])



print("\n\n***** REPETICIONES *****")
nombres = [w.lemma_.lower() for w in nlp(texto)
           if w.is_stop != True and w.is_punct != True and w.pos_ != 'CONJ' and w.pos_ != 'SPACE' and w.pos_ != 'NUM' and w.pos_ != 'ADP' and len(w) > 2]

frasesDosPalabras=[]
frasesTresPalabras=[]
i=0
#se construye arreglo de dos y tres palabras seguidas, aunque para el caso
#de dos palabras, se busca palabras repetidas que esten a la izq o der
while i < len(nombres):
    if(i==len(nombres)-1):
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i-1])
        i+=1  
    elif(i==len(nombres)-2):
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i+1])
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i-1])
        i+=1  
    elif(i==0):
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i+1])  
        i+=1   
    else:
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i+1])
        frasesDosPalabras.append(nombres[i] +" "+ nombres[i-1])
        frasesTresPalabras.append(nombres[i] +" "+ nombres[i+1]+" "+ nombres[i+2])
        i+=1  
    

frasesFrecuenteRepetidas=Counter(frasesDosPalabras).most_common(40)
frasesFrecuente=[]
for i in range(0, len(frasesFrecuenteRepetidas), 2):
    frasesFrecuente.append(frasesFrecuenteRepetidas[i])

print("\n30 palabras más repetidas:")
print (Counter(nombres).most_common(30))
print("\n20 juegos de dos palabras más repetidas:")
print (frasesFrecuente)
print("\n10 juegos de tres palabras más repetidas:")
print(Counter(frasesTresPalabras).most_common(10))
