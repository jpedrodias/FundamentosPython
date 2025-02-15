'''
Exercício 10 - Removendo itens
Como as tuplas são imutáveis não existem os métodos pop() nem remove(). A única
forma de removermos um elemento é usarmos a técnica de conversão em lista.
O método del() apaga toda a tupla
'''

sampletup1 = (0,1,2,3,4,5,6,7,8,9,10)
del sampletup1

try:
    print(sampletup1)
except NameError as e:
    print(e)
    # Output name 'sampletup1' is not defined