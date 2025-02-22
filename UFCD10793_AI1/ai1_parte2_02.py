'''
Avaliação Intermédia 1 - Parte 2 - Exercício 2

Modificar o exercício anterior para exibir o conteúdo linha por linha.
'''

filename = "data/exemplo.txt"
with open(filename, "r") as ficheiro:
    for linha in ficheiro:
        print(linha.strip())
