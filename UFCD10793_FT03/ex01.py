'''
Exercício 1 - Execussão condicional
Escreve um programa que solicite um número inteiro ao utilizador e caso o mesmo seja maior que 20, devolva o resultado da sua divisão por 2. 
'''

# Input
num = input('Insira um número inteiro: ')
num = int(num)

# Process
if num > 20:
    result = round(num / 2, 2)
    print(f'O resultado da divisão de {num} por 2 é {result}')
else:
    print(f'O número {num} não é maior que 20.')

