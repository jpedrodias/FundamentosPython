'''
Exercício 1 - match - mês
Faz um programa que escreva o nome do mês que é introduzido, pelo utilizador, na forma numérica.
'''

mes_input = input('Introduza o número do mês: ')
mes_int = int(mes_input)

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
    case _: # default
        mes_str = 'Mês inválido'

print(mes_str)
