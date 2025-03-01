'''
Exercício 1 - Bloco try/finally
'''

# Bloco finally

import sys

item = 22

try:
    divisao = 1 / item
    print('Valor:', item)
except TypeError:
    # Manipular tipo incorreto
    print('Você deve digitar apenas números!')
    print()
except ZeroDivisionError:
    # Manipular divisão por zero
    print('Não é possível dividir por zero.')
    print()
except:
    # Manipular outras exceções
    print('Ocorreu a exceção:', sys.exc_info()[0])
    print()
else:
    print('1 dividido por', item, 'é', divisao)
finally:
    print('O valor fornecido foi:', item)
