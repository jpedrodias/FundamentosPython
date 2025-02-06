'''
Exercício 19 - loops
Escreve um programa que solicite ao utilizador um número e escreva em simultâneo a sequência crescente e decrescente entre 1 e esse número.
'''

# Input
numero = int(input('Insira um número: '))
numero = int(numero)

MIN = 1
MAX = numero
print('↑ ↓')
for i in range(MIN, MAX+1):
    print(f'{i} {MAX - i + 1}')
