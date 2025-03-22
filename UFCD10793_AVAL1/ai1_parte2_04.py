'''
Avaliação Intermédia 1 - Parte 2 - Exercício 4

Modificar o programa anterior para acrescentar mais uma linha ao ficheiro.
'''

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

NEW_LINE = "\n"

filename = "data/novo_ficheiro.txt"
with open(filename, "a") as ficheiro:
    ficheiro.write("Linha adicional" + NEW_LINE)