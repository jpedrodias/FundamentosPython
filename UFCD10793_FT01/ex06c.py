'''
Exercício 6 - calcula o total de segundos (versão usando modulo datetime)

Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e
converta o resultado para segundos, devolvendo o output para o ecrã (deverá ser
criado o ficheiro ex06.py).
'''

horas_str = input('Introduza as horas no formato hh:mm:ss ')
if horas_str == '':
    horas_str = '01:00:05'


# Solução 1: insere as horas no formato hh:mm:ss fazer split à string
horas, minutos, segundos = map(int, horas_str.split(':'))
total_segundos = horas * 3600 + minutos * 60 + segundos
print(f'{horas} horas, {minutos} minutos e {segundos} segundos correspondem a {total_segundos} segundos')


# Solução 2: insere as horas no formato hh:mm:ss e comverter para um objeto datetime
from datetime import datetime

horas_str = input('Introduza as horas no formato hh:mm:ss ')
horas_dt = datetime.strptime(horas_str, '%H:%M:%S')

horas = horas_dt.hour
minutos = horas_dt.minute
segundos = horas_dt.second

total_segundos =horas * 3600 + minutos * 60 + segundos

print(f'{horas} horas, {minutos} minutos e {segundos} segundos correspondem a {total_segundos} segundos')
