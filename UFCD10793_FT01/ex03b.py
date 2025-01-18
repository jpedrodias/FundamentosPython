'''
Cria agora um nove ficheiro python (extensão .py) com o nome ex03.
Dentro deste ficheiro escreve um programa que receba, como parâmetro um inteiro, e devolva o se dobro

exemplo:
python ex03.py 5 7 9 ... etc
'''

# Para obter os parâmetros passados na linha de comandos
import sys

def calcula_dobro_de(x):
    __doc__ = 'Devolve o dobro de um número inteiro'
    return x * 2


if __name__ == '__main__':
    #print(sys.argv)
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                value = int(arg)
            except ValueError:
                value = None

            if value is not None:
                print(f'O dobro de {arg} é {calcula_dobro_de(value)}')
            else:
                print(f'Número inválido: {arg}')
        #end for
    #end if argcs
#end if __main__
