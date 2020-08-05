import spacy
from spacy import displacy
from collections import Counter

import nltk
from nltk import SnowballStemmer

spanishstemmer=SnowballStemmer("spanish")


nlp = spacy.load("es_core_news_sm")


palabrasClaveTemas="""Gobiernos gobernante gobernador secretarias secretario centros universidades escuelas institutos ministerios gobiernos alcaldías republica secretaria subsecretaria viceministerio director gerente dueño propietario"""


temasPosibles=nlp(palabrasClaveTemas)
palabrasLemitizadas = [tok.lemma_.lower() for tok in temasPosibles]


raicesPalabras = [spanishstemmer.stem(token) for token in palabrasLemitizadas]



print(list(Counter(raicesPalabras)))



