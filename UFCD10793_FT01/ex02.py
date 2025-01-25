'''
Exercício 2 - modulo math + formatação de strings

Módulo math
import math | from math import sqrt
- permite aceder a funções matemáticas

Mais sobre Strings
https://docs.python.org/pt-br/3.13/tutorial/inputoutput.html

'''

from math import sqrt

numero = int(input('Digite um \"número\" inteiro:\n '))
raizquadrada = sqrt(numero)

# Print com multiplos argumentos
print('A raiz quadrada de', numero, 'é', round(raizquadrada, 2))

# Formatação da String com format
print('A raiz quadrada de {} é {:.2f}'.format(numero, raizquadrada))

# Formatação da String com fString
print(f"A raiz quadrada de {numero} é {raizquadrada:.2f}")