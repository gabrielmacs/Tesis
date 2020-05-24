import spacy,os,json,nltk
from spacy import displacy
from collections import Counter
from nltk import SnowballStemmer

class Resumen:
    nlp = spacy.load("es_core_news_sm")
    spanishstemmer=SnowballStemmer("spanish")
    palabrasClave = []
    doc = ''
    listaPalabrasLematizadas=[]
    entMiscEvNacProdObr=[]
    etiquetadas=[]
    frasesDosPalabras = []
    frasesTresPalabras = []
    frasesTresPalabrasNoRepetidas = []
    frasesDosPalabrasNoRepetidas = []
    palabrasEtiquetadasRepetidas = []
    autoresStemming = []



    def __init__(self, palabrasClave, texto):
        self.palabrasClave = palabrasClave
        self.doc = self.nlp(texto)
        self.lematizarPalabras()
        self.etiquetarPalabras()

    def etiquetarPalabras(self):
        for e in self.doc.ents:
            if e .label_=='MISC':
                self.entMiscEvNacProdObr.append(e)
            elif (e.label_ !='DATE' and e.label_ != 'CARDINAL' and e.label_ != 'ORDINAL' and e.label_ != 'PERCENT' and e.label_ != 'QUANTITY'):
                self.etiquetadas.append(e)
        self.etiquetadasRepetidas()

    def etiquetadasRepetidas(self):
        autoresTotales = Counter(self.etiquetadas)
        for at in autoresTotales:
            if(autoresTotales[at] > 2):
                self.palabrasEtiquetadasRepetidas.append(at)
        
    def lematizarPalabras(self):
        self.listaPalabrasLematizadas = [w.lemma_.lower() for w in self.doc
           if w.is_stop != True and w.is_punct != True and w.pos_ != 'CONJ' and w.pos_ != 'SPACE' and w.pos_ != 'NUM' and w.pos_ != 'ADP' and len(w) > 2]
        self.raizPalabra()

    def raizPalabra(self):
        raicesPalabras = [self.spanishstemmer.stem(token) for token in self.listaPalabrasLematizadas]
        for i, rp in enumerate(raicesPalabras):
            for pc in self.palabrasClave:
                if rp == pc:
                    self.autoresStemming.append(self.listaPalabrasLematizadas[i]+" "+self.listaPalabrasLematizadas[i+1]+" "+self.listaPalabrasLematizadas[i+2])
        self.juegosPalabras()

    def juegosPalabras(self):
        i = 0
        while i < len(self.listaPalabrasLematizadas):
            if(i == len(self.listaPalabrasLematizadas)-1):
                self.frasesDosPalabras.append(self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i-1])
                i += 1
            elif(i == len(self.listaPalabrasLematizadas)-2):
                self.frasesDosPalabras.append(self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i+1])
                self.frasesDosPalabras.append(self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i-1])
                i += 1
            elif(i == 0):
                self.frasesDosPalabras.append(self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i+1])
                i += 1
            else: 
                self.frasesDosPalabras.append(self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i+1])
                self.frasesDosPalabras.append(self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i-1])
                self.frasesTresPalabras.append(self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i+1]+" " + self.listaPalabrasLematizadas[i+2])
                i += 1
        self.tresPalabrasNoRepetidas()

    def tresPalabrasNoRepetidas(self):
        jurgosTresPalabras = Counter(self.frasesTresPalabras).most_common(10)
        for j in jurgosTresPalabras:
           self.frasesTresPalabrasNoRepetidas.append(j[0])
        self.dosPalabrasNoRepetidas()

    def dosPalabrasNoRepetidas(self):
        frasesFrecuenteRepetidas = Counter(self.frasesDosPalabras).most_common(40)
        for i in range(0, len(frasesFrecuenteRepetidas), 2):
            self.frasesDosPalabrasNoRepetidas.append(frasesFrecuenteRepetidas[i][0])

noticia= Resumen(['gobi', 'gobern', 'secretari', 'centr', 'univers', 'escuel', 'institut', 'ministeri','gobiern', 'alcald', 'republ', 'subsecretari', 'viceministeri', 'director', 'gerent', 'dueñ', 'propietari'],"""Autoridades sanitarias de México reportaron este viernes 28 de febrero del 2020 el tercer caso del nuevo coronavirus, al confirmar un nuevo infectado en la capital, que también dio positivo a las pruebas de laboratorio luego de viajar a Italia. “Hasta este momento tenemos tres casos confirmados del nuevo coronavirus. Probablemente los tres se contagiaron de una misma fuente. Los tres son casos importados”, dijo José Luis Alomía, director general de epidemiología de México, en una conferencia de prensa. Horas antes, el Gobierno de Sinaloa, estado del noroeste de México, confirmó el segundo caso de coronavirus en el país, tras realizarle una segunda prueba a un paciente que estuvo también en Italia con el hombre de Ciudad de México que fue el primer contagio conocido en el territorio. \"En Culiacán (capital del estado) hay un caso confirmado de Covid-19, se han seguido todos los protocolos de contención y no debería de pasar a mayores. Estemos pendientes\", escribió en Twitter el gobernador Quirino Ordaz tras una reunión con la Secretaría de Salud estatal. El paciente de 41 años, originario del céntrico estado de Hidalgo, voló desde Ciudad de México a Culiacán, donde estuvo aislado en un hotel en el que se realizaban las dos pruebas confirmatorias. En la misma red social, el secretario de Salud del estado, Efrén Encinas, afirmó tener \"todo contenido y aislado\" en coordinación con la Secretaría de Salud federal y estar preparado para \"atender cualquier caso\". \"A cuidarnos. Seguimos con un caso de Covid-19 confirmado en Sinaloa, pero bien atendido y sin peligro de más contagios\", publicó el funcionario estatal. Horas antes, cuando el caso apenas era sospechoso, el también médico había ofrecido una rueda de prensa en la que explicó que el paciente padecía una sintomatología leve, con un poco de fiebre y dolor de cabeza. Precisó que este caso está relacionado con el caso positivo que se dio en Ciudad de México porque ambas personas estuvieron días antes en un congreso en el norte de Italia, al asegurar que esta persona estaba en Culiacán para dar una conferencia relacionada con su trabajo. Durante la conferencia matutina del presidente de México, Andrés Manuel López Obrador, las autoridades federales confirmaron este viernes el primer caso de coronavirus del país, el segundo detectado en América Latina después del reportado en Brasil. Hugo López-Gatell, subsecretario de Prevención y Promoción de la Salud, señaló que el positivo pertenece a un hombre de 35 años que está hospitalizado en el Instituto Nacional de Enfermedades Respiratorias (INER). Los dos primeros casos están relacionados con un mexicano residente en Bérgamo, en el norte de Italia, lugar donde se produjeron los contagios en la tercera semana de febrero. Aunque los funcionarios de salud han pedido evitar el pánico, recomiendan a la población lavarse las manos de manera constante, tapar su boca al toser o estornudar, evitar tocarse la cara y no saludar de abrazo o de beso a las personas desconocidas. También han alertado por noticias falsas que se difunden por redes sociales, por lo que exhortan a solo hacer caso a fuentes oficiales.
""")
print(noticia.frasesDosPalabrasNoRepetidas)

