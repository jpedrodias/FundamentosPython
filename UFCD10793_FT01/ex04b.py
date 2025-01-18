'''
Escreve um programa que calcule o volume de uma esfera. O valor do raio deverá ser
introduzido pelo utilizador (deverá ser criado o ficheiro ex04.py).
'''

from math import pi as PI


def calcula_volume_esfera(raio):
    __doc__ = 'Calcula o volume de uma esfera'
    return (4/3) * PI * raio**3


if __name__ == '__main__':
    raio_str = input('Introduza o raio da esfera: ')
    try:
        raio = float(raio_str)
    except ValueError:
        raio = None
    
    if raio is not None:
        volume = calcula_volume_esfera(raio)
        print(f'O volume da esfera é {volume:.2f}')
    else:
        print(f'Valor inválido: {raio_str}')
#end if main
