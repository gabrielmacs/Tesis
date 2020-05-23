import json


with open('Git/noticias/noticias.json') as file:
    data = json.load(file)
    for noticia in data['noticias']:
        print('Diario:', noticia['Diario'])
        
