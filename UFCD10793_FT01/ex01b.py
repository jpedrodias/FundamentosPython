'''
Exercício 1b - modulo math + fString

Módulo math
import math | from math import sqrt
- permite aceder a funções matemáticas

'''
from math import sqrt

numero = int(input("Digite um número: "))
raizquadrada = sqrt(numero)

print(f"A raiz quadrada de {numero} é {raizquadrada:.2f}")
