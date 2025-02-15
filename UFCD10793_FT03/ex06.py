'''
Exercício 6 - Execussão condicional e operadores de comparação
Escreve um programa que receba três números reais e indique qual o maior dos três números.
'''

# Input
num1 = input('Insira um número real: ')
num2 = input('Insira outro número real: ')
num3 = input('Insira outro número real: ')

# Converte os números para reais
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

# Process
if num1 > num2 and num1 > num3:
    print(f'O número {num1} é o maior dos três números.')   
elif num2 > num1 and num2 > num3:
    print(f'O número {num2} é o maior dos três números.')
elif num3 > num1 and num3 > num2:
    print(f'O número {num3} é o maior dos três números.')
else:
    print(f'Os números {num1}, {num2} e {num3} são iguais.')


# ALTERNATIVA:
maior = max(num1, num2, num3)
if num1 == num2 == num3:
    print(f'Os números {num1}, {num2} e {num3} são iguais')
else:
    print(f'O número {maior} é o maior dos três números.')
