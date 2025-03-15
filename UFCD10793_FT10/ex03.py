'''
Exercício 3 - Strings, split e datetime

Escreve um programa em Python que
a. Armazene as diferentes datas numa string;
b. Imprima as datas correspondentes ao ano de 2022;
c. Crie uma nova lista (dias) e na mesma armazena o dia de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
'''

datas = '12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022'

# a. Armazene as diferentes datas numa string;
datas_separadas = datas.split(',')
print('a)', datas_separadas)


# b. Imprima as datas correspondentes ao ano de 2022;
datas_2022 = []
for data in datas_separadas:
    if data.endswith('2022'):    # ou data[-4:  ? ] == '2022'
        datas_2022.append(data)
print('b)', datas_2022)


# c. Crie uma nova lista (dias) e na mesma armazena o dia de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
dias = []
for data in datas_separadas:
    dia = data[0:2]     # 0:2 é o mesmo que do indice 0 até ao indice 2 (exclusivo)
    dias.append(dia)
dias.sort()             # usei o método .sort em vez do sorted(dias) devolve uma nova lista ordenada
print('c)', dias)


# d. (EXTRA) Crie uma nova lista (meses) e na mesma armazena o mês de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
meses = []
for data in datas_separadas:
    mes = data[2:-4]  # 12jan2022
    meses.append(mes)
meses.sort()
print('d)', meses)


# O mesmo exercício mas usando datetime
import locale
from datetime import datetime
print('\n\nUsando modulo datetime')

# Definir o idioma como português (importante porque os textos estão em português)
locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')


# a. Armazene as diferentes datas numa string;
for index, data_string in enumerate(datas_separadas):
    data = datetime.strptime(data_string, '%d%b%Y')
    datas_separadas[index] = data
print('a)', datas_separadas)


# b. Imprima as datas correspondentes ao ano de 2022;
datas_2022 = []
for data in datas_separadas:
    if data.year == 2022:
        datas_2022.append(data)
print('b)', datas_2022)


# c. Crie uma nova lista (dias) e na mesma armazena o dia de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
dias = []
for data in datas_separadas:
    dias.append(data.day)
dias.sort()
print('c)', dias)


# d. (EXTRA) Crie uma nova lista (meses) e na mesma armazena o mês de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
meses = []
for data in datas_separadas:
    meses.append(data.month)
meses.sort()
print('d', meses)