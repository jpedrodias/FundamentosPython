'''
Exercício 18 - loops modulo da divisão inteira
Elabore um programa que calcule e mostre no ecrã os números pares entre 1 e 200.
'''

MIN = 1
MAX = 200
for i in range(MIN, MAX+1):
    if i % 2 == 0:
        print(i, end=' ')
