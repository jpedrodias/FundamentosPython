'''
Exercício 1 - FAV Enunciado Geral

Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para três variáveis inteiras.
'''

# lê uma data no formato DD/MM/AAAA
#data_str = input("Insere uma data no formato DD/MM/AAAA: ")
data_str = '05/04/2025'


# Sem utilizar módulos
# separa a data em dia, mês e ano
dia_str, mes_str, ano_str = data_str.split("/")
dia, mes, ano = map(int, [dia_str, mes_str, ano_str])

print(f'{ano:4d}-{mes:02d}-{dia:02d}')


# ALTERNATIVA USANDO módulo datetime
from datetime import datetime

try:
    data = datetime.strptime(data_str, "%d/%m/%Y")
except ValueError:
    data = None

if data:
    print(data.strftime("%Y-%m-%d"))
else:
    print("Data inválida")