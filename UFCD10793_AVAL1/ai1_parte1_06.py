'''
Avaliação Intermédia 1 - Parte 1 - Exercício 6

Elabora uma script em python que peça ao utilizador dois números e devolva a divisão do primeiro número introduzido pelo seguinte. 
Trate erros como divisão por zero e valores inválidos
'''

from ai1_mytools import better_input

print(__doc__)

number_a = better_input("Digite o primeiro número inteiro: ", 'Erro: Apenas números inteiros são permitidos.')
number_b = better_input("Digite o segundo número inteiro: ", 'Erro: Apenas números inteiros são permitidos.', not_allowed={}) # permite a inserção de zero para testar a divisão por zero

try:
    result = number_a / number_b
    print('A divisão de', number_a, 'por', number_b, 'é', result)
except ZeroDivisionError:
    print('Não é possível a divisão de por zero')
finally:
    pass
