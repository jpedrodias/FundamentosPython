'''
Exercício 4 - Execussão condicional e operadores de comparação maior ou menor que
Escreve um programa que receba dois números reais e indique qual o maior dos dois  números. Considera a possibilidade de o utilizador indicar dois números iguais.
'''

# Input
num1 = input('Insira um número real: ')
num2 = input('Insira outro número real: ')

# Converte os números para reais
num1, num2 = float(num1), float(num2)

if num1 == num2:
    print(f'Os números são igual')
else:
    maior = max(num1, num2)
    print(f'O número {maior} é maior')