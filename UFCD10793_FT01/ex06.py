'''
Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e
converta o resultado para segundos, devolvendo o output para o ecrã (deverá ser
criado o ficheiro ex06.py).

exemplo:
python ex06.py 1 10 20
devolve 3600 + 60 + 20 = 4220
'''

import sys

def converte_para_segundos(horas, minutos, segundos):
    __doc__ = 'Converte horas, minutos e segundos para segundos'
    return horas * 3600 + minutos * 60 + segundos

if __name__ == '__main__':
    if len(sys.argv) == 4:
        print(sys.argv[1:])
        horas, minutos, segundos = [int(i) for i in sys.argv[1:]]
        print(horas, minutos, segundos)
        try:
            horas, minutos, segundos = [int(i) for i in sys.argv[1:]]
        except ValueError: 
            horas, minutos, segundos = [None, None, None]

        if horas is None or minutos is None or segundos is None:
            print('Valores inválidos')
        else:
            total_segundos = converte_para_segundos(horas, minutos, segundos)
            print(f'{horas} horas, {minutos} minutos e {segundos} segundos correspondem a {total_segundos} segundos')
    else:
        print('Número de argumentos inválido\nExemplo: python ex06.py 1 10 20')