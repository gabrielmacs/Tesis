import spacy
import os
import json
import nltk
from spacy import displacy
from collections import Counter
from nltk import SnowballStemmer


class Resumen:
    nlp = spacy.load("en_core_web_sm")
    spanishstemmer = SnowballStemmer("english")
    palabrasClave = []
    doc = ''
    ubicaciones = ''
    listaPalabrasLematizadas = []
    entMiscEvNacProdObr = []
    etiquetadasTodasNoMisc = []
    frasesDosPalabras = []
    frasesTresPalabras = []
    frasesTresPalabrasNoRepetidas = []
    frasesDosPalabrasNoRepetidas = []
    palabrasEtiquetadasRepetidas = []
    actoresStemming = []
    idioma=''

    # variables auxiliares
    posicionesParaBorrarEnLemma = []

    def __init__(self, idioma):
        self.idioma=idioma
        if(idioma == "EN"):
            print("idioma: Ingles++++++++++++++++++++++++++++")
            self.nlp = spacy.load("en_core_web_sm")
            self.spanishstemmer = SnowballStemmer("english")
        elif(idioma == "ES"):
            print("idioma: español***********************")
            self.nlp = spacy.load("es_core_news_sm")
            self.spanishstemmer = SnowballStemmer("spanish")

        self.doc = ''
        self.listaPalabrasLematizadas = []
        self.entMiscEvNacProdObr = []
        self.etiquetadasTodasNoMisc = []
        self.frasesDosPalabras = []
        self.frasesTresPalabras = []
        self.frasesTresPalabrasNoRepetidas = []
        self.frasesDosPalabrasNoRepetidas = []
        self.palabrasEtiquetadasRepetidas = []
        self.actoresStemming = []
        self.posicionesParaBorrarEnLemma = []

    def procesarPalabrasClave(self, palabrasClaveRecibidas):
        if(palabrasClaveRecibidas != ""):
            self.palabrasClave = palabrasClaveRecibidas
            print(self.palabrasClave)

    def procesarTexto(self, texto):
        self.doc = ''
        self.listaPalabrasLematizadas = []
        self.entMiscEvNacProdObr = []
        self.etiquetadasTodasNoMisc = []
        self.frasesDosPalabras = []
        self.frasesTresPalabras = []
        self.frasesTresPalabrasNoRepetidas = []
        self.frasesDosPalabrasNoRepetidas = []
        self.palabrasEtiquetadasRepetidas = []
        self.actoresStemming = []
        self.posicionesParaBorrarEnLemma = []
        if(texto != ""):
            self.doc = self.nlp(texto)
            self.getUbicaciones()

    def etiquetarPalabras(self):

        for e in self.doc.ents:
            if e .label_ == 'MISC':
                self.entMiscEvNacProdObr.append(e)
            elif (e.label_ != 'DATE' and e.label_ != 'CARDINAL' and e.label_ != 'ORDINAL' and e.label_ != 'PERCENT' and e.label_ != 'QUANTITY'):
                self.etiquetadasTodasNoMisc.append(e)
        self.etiquetadasRepetidas()

    def etiquetadasRepetidas(self):
        actoresTotales = Counter(self.etiquetadasTodasNoMisc)
        for at in actoresTotales:
            if(actoresTotales[at] > 2):
                self.palabrasEtiquetadasRepetidas.append(at)

    def getUbicaciones(self):
        if(self.idioma == "EN"):
            for en in self.doc.ents:
                if en.label_ == 'ORG' or en.label_ == 'PER' or en.label_ == 'MISC' :
                    self.actoresStemming.append(
                        en.text.strip())
        elif(self.idioma == "ES"):       
            for en in self.doc.ents:
                if en.label_ == 'ORG' :
                    self.actoresStemming.append(
                        en.text.strip())

        self.ubicaciones = [e[0] for e in self.doc.ents
                            if e.label_ != 'MISC' and e.label_ != 'PER' and e.label_ != 'ORG']
        self.lematizarPalabras()

    def lematizarPalabras(self):
        for w in self.doc:
            for u in self.ubicaciones:
                if w.text == u.text:
                    continue
            if (w.is_stop != True and w.is_punct != True and w.pos_ != 'CONJ' and w.pos_ != 'SPACE' and w.pos_ != 'SYM' and w.pos_ != 'SCONJ' and w.pos_ != 'PUNCT' and w.pos_ != 'INTJ' and w.pos_ != 'NUM' and w.pos_ != 'ADP' and len(w) > 2):
                self.listaPalabrasLematizadas.append(w.lemma_.lower())

        self.raizPalabra()

    def raizPalabra(self):
        raicesPalabras = [self.spanishstemmer.stem(
            token) for token in self.listaPalabrasLematizadas]
        i = 0
        while i < len(raicesPalabras):
            for pc in self.palabrasClave:
                if raicesPalabras[i] == pc:
                    if i+3 == len(raicesPalabras):
                        self.actoresStemming.append(
                            self.listaPalabrasLematizadas[i]+" "+self.listaPalabrasLematizadas[i+1])
                    if i+2 >= len(raicesPalabras):
                        break
                    else:
                        self.actoresStemming.append(
                            self.listaPalabrasLematizadas[i]+" "+self.listaPalabrasLematizadas[i+1]+" "+self.listaPalabrasLematizadas[i+2])
                        self.actoresStemming.append(
                            self.listaPalabrasLematizadas[i]+" "+self.listaPalabrasLematizadas[i+1])
                    self.posicionesParaBorrarEnLemma.append(
                        self.listaPalabrasLematizadas[i])
                    i += 1
                    break
            i += 1
        self.quitarPalabrasUsadasEnRaiz()

    def quitarPalabrasUsadasEnRaiz(self):
        if(len(self.posicionesParaBorrarEnLemma) > 0):
            for i in self.posicionesParaBorrarEnLemma:
                self.listaPalabrasLematizadas.remove(i)
        self.juegosPalabras()

    def juegosPalabras(self):
        i = 0
        while i < len(self.listaPalabrasLematizadas):
            if(i == len(self.listaPalabrasLematizadas)-1):
                self.frasesDosPalabras.append(
                    self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i-1])
                i += 1
            elif(i == len(self.listaPalabrasLematizadas)-2):
                self.frasesDosPalabras.append(
                    self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i+1])
                self.frasesDosPalabras.append(
                    self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i-1])
                i += 1
            elif(i == 0):
                self.frasesDosPalabras.append(
                    self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i+1])
                i += 1
            else:
                self.frasesDosPalabras.append(
                    self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i+1])
                self.frasesDosPalabras.append(
                    self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i-1])
                self.frasesTresPalabras.append(
                    self.listaPalabrasLematizadas[i] + " " + self.listaPalabrasLematizadas[i+1]+" " + self.listaPalabrasLematizadas[i+2])
                i += 1
        self.dosPalabrasNoRepetidas()

    def dosPalabrasNoRepetidas(self):
        frasesFrecuenteRepetidas = self.frasesDosPalabras
        for i in range(1, len(frasesFrecuenteRepetidas), 2):
            self.frasesDosPalabrasNoRepetidas.append(
                frasesFrecuenteRepetidas[i])


"""
    def tresPalabrasNoRepetidas(self):
        jurgosTresPalabras = Counter(self.frasesTresPalabras).most_common(10)
        for j in jurgosTresPalabras:
            if(j[1]>1):
                self.frasesTresPalabrasNoRepetidas.append(j)
        self.dosPalabrasNoRepetidas()
"""
