import os
import xlrd
import json
from datetime import datetime

nombreArchivoExcel = "200425-CorpusPrensaElComercioEC.xlsx"
nombreArchivoJSON = "noticias.json"
rutaActualpy = os.path.dirname(os.path.abspath(__file__))
# os.path.dirname(os.path.abspath(__file__)) obtiene la ruta del archivo actual
pathArchivoExcel = os.path.join(rutaActualpy, nombreArchivoExcel)
pathArchivoJSON = os.path.join(rutaActualpy, nombreArchivoJSON)
archivoAbierto = xlrd.open_workbook(pathArchivoExcel)
hojaDeTrabajo = archivoAbierto.sheet_by_name("ElComercioEC")


data = {}
data['noticias'] = []

i = 2
while i < hojaDeTrabajo.nrows:
    fecha = xlrd.xldate_as_tuple(hojaDeTrabajo.cell_value(i, 2), archivoAbierto.datemode)
    fechaFormateada=str(fecha[0])+"-"+str(fecha[1])+"-"+str(fecha[2])
    data['noticias'].append({
        'Diario': hojaDeTrabajo.cell_value(i, 0),
        'Pais': hojaDeTrabajo.cell_value(i, 1),
        'Fecha': fechaFormateada,
        'Titulo': hojaDeTrabajo.cell_value(i, 3),
        'Texto': hojaDeTrabajo.cell_value(i, 4)
    })
    i += 1


with open(pathArchivoJSON, 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
