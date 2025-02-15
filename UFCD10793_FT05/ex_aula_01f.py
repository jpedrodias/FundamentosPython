'''
Exercício 1f - listas tamanho
Escreve um programa, em python, que verifique se uma lista é vazia ou não.
Caso a lista seja vazia, mostre True, caso contrário False.
'''

lista = []
if not len(lista) > 0:
    print('Lista vazia.')
else:
    print('A lista não é vazia.')