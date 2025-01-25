'''
Exercício 6 - calcula o total de segundos

Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e
converta o resultado para segundos, devolvendo o output para o ecrã (deverá ser
criado o ficheiro ex06.py).
'''

horas = int(input('Introduza as horas: '))
minutos = int(input('Introduza os minutos: '))
segundos = int(input('Introduza os segundos: '))
total_segundos = horas * 3600 + minutos * 60 + segundos
print(f'{horas} horas, {minutos} minutos e {segundos} segundos correspondem a {total_segundos} segundos')
