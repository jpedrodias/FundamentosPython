'''
Exercício 3 - funções
Escreve uma função em Python que dada uma lista de números imprime a soma
dos valores dessa lista, o número de elementos da lista e a media desses
valores.
'''

def lista_numeros(lista):
    soma = sum(lista)
    elementos = len(lista)
    media = soma / elementos
    print('Lista:', lista)
    print(' * Soma:', soma)
    print(' * Elementos:', elementos)
    print(' * Média:', media)

# Testes
lista_numeros([1, 2, 3, 4, 5]) # Soma: 15 Elementos: 5 Média: 3.0
lista_numeros([10, 20, 30, 40, 50]) # Soma: 150 Elementos: 5 Média: 30.0
lista_numeros([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Soma: 55 Elementos: 10 Média: 5.5  