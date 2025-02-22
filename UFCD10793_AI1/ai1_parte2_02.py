'''
Avaliação Intermédia 1 - Parte 2 - Exercício 2

Modificar o exercício anterior para exibir o conteúdo linha por linha.
'''

with open("exemplo.txt", "r") as ficheiro:
    for linha in ficheiro:
        print(linha.strip())
