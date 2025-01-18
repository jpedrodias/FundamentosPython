'''
Faz um programa que receba a distância em km e a quantidade em litros de
combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve
uma mensagem de acordo com o resultado obtido. (deverá ser criado o ficheiro
ex07.py).

Exemplo: python ex07.py 100 10
'''

import sys

def calcula_consumo(distancia, litros, precisao=2):
    __doc__ = 'Calcula o consumo em km/l'
    return round(distancia / litros, precisao)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            distancia, litros = [float(f) for f in sys.argv[1:]]
        except ValueError:
            distancia, litros = None, None

        if distancia is not None and litros is not None:
            consumo = calcula_consumo(distancia, litros)
            print(f'O consumo foi de {consumo} km/l')
        else:
            print('Valores inválidos\nExemplo: python ex07.py 100 10')
    else:
        print('Número de argumentos inválido\nExemplo: python ex07.py 100 10')
#end if __main__