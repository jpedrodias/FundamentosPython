'''
Exercício 10 - Calculadora simples usando o match
Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores. 
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da operação desejada. 
'''

operacao = input('Insira a operação desejada (+, -, *, /): ')
num1 = input('Insira um número: ')
num2 = input('Insira outro número: ')

# Converte as string para números para reais
num1 = float(num1)
num2 = float(num2)

match operacao:
    case '+':
        operacao = 'adição'
        resultado = num1 + num2
    case '-':
        operacao = 'subtração'
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
        operacao = 'multiplicação'
    case '/':
        operacao = 'divisão'
        if num2 == 0:
            resultado = 'impossível de cacular. Não é possível dividir por zero.'
        else:
            resultado = num1 / num2
    case _: 
        resultado = None

if resultado:
    print(f'O resultado da {operacao} é {resultado}.')
else:
    print('Operação inválida. Insira uma operação válida (+, -, *, /).')