'''
Exercício 12 - while loop - fatorial
Escreve um programa que calcule a soma e o produto dos N primeiros números naturais.
'''

numero = int(input('Calculo do fatorial. Qual o o número (positivo)? '))

fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i += 1
print(f'O fatorial de {numero} é {fatorial}.')
