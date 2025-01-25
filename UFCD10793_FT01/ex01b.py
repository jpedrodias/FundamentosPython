'''
Exercício 1b - modulo math + fString

Módulo math
import math | from math import sqrt
- permite aceder a funções matemáticas

Mais sobre Strings
https://docs.python.org/pt-br/3.13/tutorial/inputoutput.html

'''
from math import sqrt

numero = int(input("Digite um número: "))
raizquadrada = sqrt(numero)

print(f"A raiz quadrada de {numero} é {raizquadrada:.2f}")
