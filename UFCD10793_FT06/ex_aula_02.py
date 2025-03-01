'''
Exercício 2 - listas
Considera a lista: notas = [11.2, 15, 8.7, 17.2, 7.9 ]

Cria um programa, em python, que:
    a. Acrescenta o valor 10.9 no final da lista e faz o print de toda a lista
    b. Faz o print do tamanho da lista
    c. Faz o print do valor mínimo da lista
    d. Faz a média dos valores da lista
'''

notas = [11.2, 15, 8.7, 17.2, 7.9]

# a. Acrescenta o valor 10.9 no final da lista e faz o print de toda a lista
notas.append(10.9)
print(notas)

# b. Faz o print do tamanho da lista
print('Tamanho da lista', len(notas))

# c. Faz o print do valor mínimo da lista
print('Valor mínimo na lista', min(notas))

# d. Faz a média dos valores da lista
media = sum(notas) / len(notas)
print(f'Média dos valores da lista {media:0.2f}')