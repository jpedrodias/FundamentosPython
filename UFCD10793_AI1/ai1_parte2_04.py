'''
Avaliação Intermédia 1 - Parte 2 - Exercício 4

Modificar o programa anterior para acrescentar mais uma linha ao ficheiro.
'''

NEW_LINE = "\n"

filename = "z_novo_ficheiro.txt"
with open(filename, "a") as ficheiro:
    ficheiro.write("Linha adicional" + NEW_LINE)