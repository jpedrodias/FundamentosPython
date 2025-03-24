'''
Avaliação Intermédia 1 - Parte 2 - Exercício 6

Cria ou faz download de um ficheiro CSV. De seguida cria um programa que leia o ficheiro CSV e mostre cada linha do mesmo.

Ficheiro CSV retirado de https://www.kaggle.com/datasets/uciml/iris
Instalada Extensão vscode: Rainbow CSV
'''

import csv

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)


filename = 'data/kaggle_datasets_ucim_iris.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

