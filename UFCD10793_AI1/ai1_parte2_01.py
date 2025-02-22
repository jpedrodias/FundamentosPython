'''
Avaliação Intermédia 1 - Parte 2 - Exercício 1

Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo.
'''

print(__doc__, )

filename = "data/exemplo.txt"
with open(filename, "r") as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)