'''
Exercício 13 - while loop
Elabora um programa para soma todos os valores entre 10 e 100 (inclusive) e apresentar os valores
no ecrã.
'''

# Input
MIN = 10
MAX = 100
soma = 0
i = MIN
while i <= MAX:
    soma += i
    i += 1
print(f'A soma dos valores entre {MIN} e {MAX} é {soma}.')