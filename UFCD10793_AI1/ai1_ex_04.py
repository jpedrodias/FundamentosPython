'''
Avaliação Intermédia 1 - Exercício 4

Crie um programa que captura qualquer erro e exibe uma mensagem apropriada.
'''

import sys
try:
    numero = int(input('Digite um número: '))
    print('O dobro do número é', numero * 2)
except Exception as e:
    print('Error inesperado:', e)
    sys.exit(1)

