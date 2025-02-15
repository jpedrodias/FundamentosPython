'''
Exercício 14 - for loop - soma de min a max
Elabora um programa para soma todos os valores entre 10 e 100 (inclusive) e apresentar os valores
no ecrã.
'''

MIN = int(input('Valor mínimo? '))
MAX = int(input('Valor máximo? '))
for i in range(MIN, MAX+1):
    print(i, end=' ')   
