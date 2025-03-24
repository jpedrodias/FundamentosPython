'''
Avaliação Intermédia 1 - Parte 2 - Exercício 3

Criar um programa que escreva três linhas num ficheiro novo.
'''

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

NEW_LINE = "\n"

filename = "data/novo_ficheiro.txt"
with open(filename, "w") as ficheiro:
    ficheiro.write("Linha 1" + NEW_LINE)
    ficheiro.write("Linha 2" + NEW_LINE)
    ficheiro.write("Linha 3" + NEW_LINE)

print("Ficheiro criado com sucesso.", filename)
