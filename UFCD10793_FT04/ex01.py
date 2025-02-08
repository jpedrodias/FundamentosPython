'''
Exercício 1 - match - Mês
Faz um programa que escreva o nome do mês que é introduzido, pelo utilizador, na forma numérica.
'''

# Input
mes_int = 0
while mes_int < 1 or mes_int > 12:
    mes_input = input('Insira um número inteiro entre 1 e 12: ')
    try:
        mes_int = int(mes_input)
    except ValueError:
        mes = 0

match mes_int:
    case 1:
        mes_str = 'Janeiro'
    case 2:
        mes_str = 'Fevereiro'
    case 3:
        mes_str = 'Março'
    case 4:
        mes_str = 'Abril'
    case 5:
        mes_str = 'Maio'
    case 6:
        mes_str = 'Junho'
    case 7:
        mes_str = 'Julho'
    case 8:
        mes_str = 'Agosto'
    case 9:
        mes_str = 'Setembro'
    case 10:
        mes_str = 'Outubro'
    case 11:
        mes_str = 'Novembro'
    case 12:
        mes_str = 'Dezembro'

print(mes_str)
