'''
Exercício 1 - listas
Considera a lista: cores=['amarelo', 'azul', 'branco', 'preto', 'verde']

Cria um programa, em python, que:
    a. Faz o print de toda a lista
    b. Faz o print do indíce 2 da lista
    c. Altera o indíce 0 da lista para 'vermelho'
    d. Faz o print de toda a lista
    e. Acrescenta no final da lista a cor 'amarelo'
    f. Faz o print de toda a lista
    g. Acrescenta no indíce 2 a cor 'roxo'
    h. Faz o print de toda a lista
    i. Apaga o último elemento da lista
    j. Faz o print de toda a lista
    k. Faz o print do tamanho da lista (len)
'''

cores = ['amarelo', 'azul', 'branco', 'preto', 'verde']

# a. Faz o print de toda a lista

# método 1
print('Cores:')
for cor in cores:
    print(cor, end=' ')
print()

# método 2
print('Cores:', cores)

# método 3
print('Cores:', ', '.join(cores))


# b. Faz o print do indíce 2 da lista
print('Cor no índice 2:', cores[2])

# c. Altera o indíce 0 da lista para 'vermelho'
cores[0] = 'vermelho'

# d. Faz o print de toda a lista
print('Cores:', cores)

# e. Acrescenta no final da lista a cor 'amarelo'
cores.append('amarelo')

# f. Faz o print de toda a lista
print('Cores:', cores)

# g. Acrescenta no indíce 2 a cor 'roxo'
cores.insert(2, 'roxo')

# h. Faz o print de toda a lista
print('Cores:', cores)

# i. Apaga o último elemento da lista
cores.pop()

# j. Faz o print de toda a lista
print('Cores:', cores)

# k. Faz o print do tamanho da lista (len)
print('Tamanho da lista:', len(cores))

# l. Faz o print do índice da cor 'branco'
print('Índice da cor branco:', cores.index('branco'))

# m. Faz o print do número de vezes que a cor 'amarelo' aparece na lista
print('Número de vezes que a cor amarelo aparece:', cores.count('amarelo'))

# n. Faz o print da lista invertida
print('Lista invertida:', cores[::-1])

# o. Faz o print da lista ordenada
cores.sort()
print('Lista ordenada:', cores)

# p. Faz o print da lista ordenada inversa
cores.sort(reverse=True)
print('Lista ordenada inversa:', cores)