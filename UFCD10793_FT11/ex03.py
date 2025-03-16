'''
Exercício 3 - funções com *args
Escreve uma função em Python que dada uma lista de números imprime a soma
dos valores dessa lista, o número de elementos da lista e a media desses
valores.
'''
from my_fancy_terminal import print, Colors as Cores

def lista_numeros(*lista):
    soma = sum(lista)
    elementos = len(lista)
    media = soma / elementos
    print('Lista:', lista)
    print(' * Soma:', soma)
    print(' * Elementos:', elementos)
    print(' * Média:', media)

print('LISTA DE NÚMEROS FLAT', color=Cores.RED)
lista_numeros(1, 2, 3, 4, 5) # Soma: 15 Elementos: 5 Média: 3.0
lista_numeros(10, 20, 30, 40, 50) # Soma: 150 Elementos: 5 Média: 30.0
lista_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Soma: 55 Elementos: 10 Média: 5.5 
#lista_numeros([1, 2, 3, 4, 5])


print('LISTA DE NÚMEROS 2D', color=Cores.RED)
def lista_numeros_flat(*lista):
    lista_flat = []
    for item in lista:
        if isinstance(item, (list, tuple)):
            lista_flat.extend(item)
        else:
            lista_flat.append(item)

    soma = sum(lista_flat)
    elementos = len(lista_flat)
    media = soma / elementos

    print('Lista:', lista_flat)
    print(' * Soma:', soma)
    print(' * Elementos:', elementos)
    print(' * Média:', media)

lista_numeros_flat([1, 2, 3, 4, 5])
lista_numeros_flat(1, 2, [3, 4, 5])