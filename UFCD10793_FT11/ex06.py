'''
Exercício 6 - dicionários
Escreve uma função que, dado o número do mês retorne o mesmo, por extenso.
'''

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

mes = int(input('Introduza o número do mês: '))
mes_extenso = meses.get(mes, 'Mês inválido')
print(mes_extenso)