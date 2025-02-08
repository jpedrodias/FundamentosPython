'''
Exercício 17 - loops - lazy mode
Escreva um programa que peça ao utilizador 20 números reais e no final mostre a soma e a média dos números introduzidos.
'''
LAZYMODE = True

if LAZYMODE:
    from random import random

quantidade = 20
soma = 0
for i in range(quantidade):
    if LAZYMODE:
        numero = 9 * random() + 1
        numero = round(numero, 1)
        print(f'Número real #{i+1}: {numero}')
    else:
        numero = float(input(f'Insira um número real #{i+1}: '))
    soma += numero

media = soma / quantidade
print('Soma:', round(soma, 1))
print('Média:', round(media, 1))
