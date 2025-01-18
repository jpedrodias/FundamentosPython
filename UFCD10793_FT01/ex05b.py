'''
Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor da hipotenusa (deverá ser criado o ficheiro ex05.py).
'''
from math import sqrt


def calcula_hipotenusa(a, b):
    __doc__ = 'Calcula a hipotenusa de um triângulo retângulo'
    return sqrt(a**2 + b**2)


if __name__ == '__main__':
    a_str = input('Introduza o valor do cateto a: ')
    b_str = input('Introduza o valor do cateto b: ')
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        a = None
        b = None
    
    if a is not None and b is not None:
        hipotenusa = calcula_hipotenusa(a, b)
        print(f'O valor da hipotenusa é {hipotenusa:.2f}')
    else:
        print(f'Valor inválido: {a_str} ou {b_str}')
#end if
