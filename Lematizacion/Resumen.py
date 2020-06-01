import spacy,os,json,nltk
from spacy import displacy
from collections import Counter
from nltk import SnowballStemmer

class Resumen:
    nlp = spacy.load("es_core_news_sm")
    spanishstemmer=SnowballStemmer("spanish")
    palabrasClave = ['gobi', 'gobern', 'secretari', 'centr', 'univers', 'escuel', 'institut', 'ministeri','gobiern', 'alcald', 'republ', 'subsecretari', 'viceministeri', 'director', 'gerent', 'dueñ', 'propietari']
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

    #variables auxiliares
    posicionesParaBorrarEnLemma=[]

    def __init__(self):
        self.doc = ''
        self.listaPalabrasLematizadas=[]
        self.entMiscEvNacProdObr=[]
        self.etiquetadas=[]
        self.frasesDosPalabras = []
        self.frasesTresPalabras = []
        self.frasesTresPalabrasNoRepetidas = []
        self.frasesDosPalabrasNoRepetidas = []
        self.palabrasEtiquetadasRepetidas = []
        self.autoresStemming = []
        self.posicionesParaBorrarEnLemma=[]

    def procesarPalabrasClave(self, nombreArchivoTxt):
        if(nombreArchivoTxt!=""):
            self.palabrasClave=[]
            ruta='Git/Lematizacion/'+nombreArchivoTxt
            with open(ruta) as file:
                self.palabrasClave = [self.spanishstemmer.stem(i.strip()) for i in file]
                print(self.palabrasClave)


    def procesarTexto(self,texto):
        self.doc = ''
        self.listaPalabrasLematizadas=[]
        self.entMiscEvNacProdObr=[]
        self.etiquetadas=[]
        self.frasesDosPalabras = []
        self.frasesTresPalabras = []
        self.frasesTresPalabrasNoRepetidas = []
        self.frasesDosPalabrasNoRepetidas = []
        self.palabrasEtiquetadasRepetidas = []
        self.autoresStemming = []
        self.posicionesParaBorrarEnLemma=[]
        if(texto!=""):
            self.doc = self.nlp(texto)
            self.lematizarPalabras()



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
        i=0
        while i < len(raicesPalabras):
            for pc in self.palabrasClave:
                if raicesPalabras[i] == pc:
                    if i+3 == len(raicesPalabras):
                        self.autoresStemming.append(self.listaPalabrasLematizadas[i]+" "+self.listaPalabrasLematizadas[i+1])
                    if i+2 >= len(raicesPalabras):
                        break
                    else:    
                        self.autoresStemming.append(self.listaPalabrasLematizadas[i]+" "+self.listaPalabrasLematizadas[i+1]+" "+self.listaPalabrasLematizadas[i+2])
                    self.posicionesParaBorrarEnLemma.append(self.listaPalabrasLematizadas[i])
                    i+=1
                    break
            i+=1
        self.quitarPalabrasUsadasEnRaiz()

    def quitarPalabrasUsadasEnRaiz(self):
        if(len(self.posicionesParaBorrarEnLemma)>0):
            for i in self.posicionesParaBorrarEnLemma:
                self.listaPalabrasLematizadas.remove(i)
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
           self.frasesTresPalabrasNoRepetidas.append(j)
        self.dosPalabrasNoRepetidas()

    def dosPalabrasNoRepetidas(self):
        frasesFrecuenteRepetidas = Counter(self.frasesDosPalabras).most_common(40)
        for i in range(0, len(frasesFrecuenteRepetidas), 2):
            self.frasesDosPalabrasNoRepetidas.append(frasesFrecuenteRepetidas[i])


