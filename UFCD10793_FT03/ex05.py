'''
Exercício 5 - Execussão condicional e operadores de comparação de maior ou menor que
Escreva um programa que verifique se um determinado número introduzido pelo utilizador é nulo, positivo ou negativo.
'''

# Input
num = input('Insira um número inteiro: ')
num = float(num)

# Process
if num > 0:
    print(f'O número {num} é positivo.')
elif num < 0:
    print(f'O número {num} é negativo.')
else:
    print(f'O número {num} é nulo.')