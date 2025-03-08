'''
Exercício 5 - funções
Escreve uma função em Python que, dada uma lista de elementos, devolva
essa mesma lista, mas sem elementos repetidos.
'''

def remove_repetidos_por_index(lista):
    '''Remove elementos repetidos de uma lista, mantendo o primeiro elemento
    e removendo os restantes.
    
    WARNIG: Em python as listas são passadas por referência, por isso, a lista
    original é alterada. Para manter a lista original, deve-se passar uma cópia da lista.
    '''
    to_remove = []

    new_list = lista.copy()

    for index, item in enumerate(lista):
        if lista[index:].count(item) > 1:
            to_remove.append(index)
    for index in reversed(to_remove):
        new_list.pop(index)
    return new_list

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
new_list = remove_repetidos_por_index(lista)
    
print(lista)
print(new_list)