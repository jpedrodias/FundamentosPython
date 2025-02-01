'''
Exercício 3 - Execussão condicional e operador módulo da divisão inteira
Escreve um programa que solicite um número inteiro ao utilizador e verifique se o mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato; 
"O número [número] é [par/ímpar]"
'''


# Input
num = input('Insira um número inteiro: ')
num = int(num)

# Process
if num % 2 == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')
