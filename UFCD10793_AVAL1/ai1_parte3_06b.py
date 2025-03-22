'''
Avaliação Intermédia 1 - Parte 3 - Exercício 6 - CRUD System com SQLite

Igual ao 2.6 mas com .sqlite em vez de csv
'''


import sqlite3, os

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

print(__doc__)

DATABASE = 'data/kaggle_datasets_ucim_iris.sqlite'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

data = {}

for line in cursor.execute('SELECT * FROM iris').fetchall():
    id, sepal_length, sepal_width, petal_length, petal_width, species = line

    if species not in data:
        data[species] = {
            'sepal_length': 0, 
            'sepal_width': 0, 
            'petal_length': 0, 
            'petal_width': 0, 
            'count': 0, 
            'average': 0}
    
    data[species]['sepal_length'] += sepal_length
    data[species]['sepal_width'] += sepal_width
    data[species]['petal_length'] += petal_length
    data[species]['petal_width'] += petal_width
    data[species]['count'] += 1

for species in data:
    sepal_length_average = round(data[species]['sepal_length'] / data[species]['count'], 2)
    sepal_width_average = round(data[species]['sepal_width'] / data[species]['count'], 2)
    petal_length_average = round(data[species]['petal_length'] / data[species]['count'], 2)
    petal_width_average = round(data[species]['petal_width'] / data[species]['count'], 2)

    data[species]['average'] = {
        'sepal_length': sepal_length_average,
        'sepal_width': sepal_width_average,
        'petal_length': petal_length_average,
        'petal_width': petal_width_average
    }

    print(f'{species}: {data[species]['average']}')