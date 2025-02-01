'''
Exercício 10 - Calculadora simples
Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores. 
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da operação desejada. 
'''


# Input
operacao = input('Insira a operação desejada (+, -, *, /): ')
num1 = input('Insira um número: ')
num2 = input('Insira outro número: ')

# Converte os números para reais
num1 = float(num1)
num2 = float(num2)

# Process
if operacao == '+':
    resultado = num1 + num2
    print(f'O resultado da soma é {resultado}.')
elif operacao == '-':
    resultado = num1 - num2
    print(f'O resultado da subtração é {resultado}.')
elif operacao == '*':
    resultado = num1 * num2
    print(f'O resultado da multiplicação é {resultado}.')
elif operacao == '/':
    if num2 == 0:
        print('Não é possível dividir por zero.')
    else:
        resultado = num1 / num2
        print(f'O resultado da divisão é {resultado}.')
else:
    print('Operação inválida. Insira uma operação válida (+, -, *, /).')
