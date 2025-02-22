'''
Avaliação Intermédia 1 - Parte 2 - Exercício 3

Criar um programa que escreva três linhas num ficheiro novo.
'''

with open("z_novo_ficheiro.txt", "w") as ficheiro:
    ficheiro.write("Linha 1")
    ficheiro.write("Linha 2")
    ficheiro.write("Linha 3")