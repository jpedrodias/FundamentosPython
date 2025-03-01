'''
Exercício 5 - funções
Escreve uma função em Python que, dada uma lista de elementos, devolva
essa mesma lista, mas sem elementos repetidos.
'''

from os import chdir, getcwd, path

print('A pasta antes de chdir', getcwd())
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

print('A pasta depois de chdir', getcwd())


def remove_repetidos(lista):
    to_remove = []
    for item in lista:
        if lista.count(item) > 1:
            to_remove.append(item)
