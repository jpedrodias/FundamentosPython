'''
Avaliação Intermédia 1 - Parte 2 - Exercício 2

Modificar o exercício anterior para exibir o conteúdo linha por linha.
'''

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

filename = "data/exemplo.txt"
with open(filename, "r") as ficheiro:
    for linha in ficheiro:
        print(linha.strip())
