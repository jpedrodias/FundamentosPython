'''
Exercício 10 - Calculadora simples usando o match
Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores. 
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da operação desejada. 
'''

operacao = input('Insira a operação desejada (+, -, *, /): ')
numero = input('Insira um número: ')
outro_numero = input('Insira outro número: ')

# Converte as string para números para reais
numero = float(numero)
outro_numero = float(outro_numero)

match operacao:
    case '+':
        operacao = 'adição'
        resultado = numero + outro_numero
    case '-':
        operacao = 'subtração'
        resultado = numero - outro_numero
    case '*':
        operacao = 'multiplicação'
        resultado = numero * outro_numero
    case '/':
        operacao = 'divisão'
        # Nested case para verificar se o denominador é zero
        match outro_numero:
            case 0:
                resultado = 'impossível de cacular. Não é possível dividir por zero.'
            case _:
                resultado = numero / outro_numero

    case _: 
        resultado = None
if resultado is None:
    print(f'O resultado da {operacao} é {resultado}.')
else:
    print('Operação inválida. Insira uma operação válida (+, -, *, /).')