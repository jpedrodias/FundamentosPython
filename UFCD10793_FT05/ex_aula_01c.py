'''
Exercício 1c - números aleatórios
c. Escreva um programa que gere 100 números reais aleatórios entre 0 e 1 e
armazene-os numa lista. No final o programa deverá mostrar as seguintes informações:
i. Maior número;
ii. Menor número;
iii. Soma de todos os números gerados;
iv. Média e desvio padrão.
'''

from random import random
from statistics import mean, stdev

lista = []

for num in range(1,101):
    lista.append(random())

print(f'Maior numero: {max(lista)}')
print(f'Menor número: {min(lista)}')
print(f'Soma dos numeros: {sum(lista)}')
print(f'Média dos numeros gerados: {mean(lista)}')
print(f'Desvio padrao dos numeros gerados: {stdev(lista)}')