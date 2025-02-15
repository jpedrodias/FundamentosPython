'''
Exercício 2 - Execussão condicional e operador de igualdade
Implementa um programa que leia dois números e indique se estes são iguais ou diferentes.
'''

# Input
num1 = input('Insira um número inteiro: ')
num2 = input('Insira outro número inteiro: ')

# Converte os números para inteiros
num1 = int(num1)
num2 = int(num2)

# Process
if num1 == num2:
    print(f'Os números {num1} e {num2} são iguais.')
else:
    print(f'Os números {num1} e {num2} são diferentes.')
