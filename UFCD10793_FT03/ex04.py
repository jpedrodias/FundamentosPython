'''
Exercício 4 - Execussão condicional e operadores de comparação
Escreve um programa que receba dois números reais e indique qual o maior dos dois  números. Considera a possibilidade de o utilizador indicar dois números iguais.
'''

# Input
num1 = input("Insira um número real: ")
num2 = input("Insira outro número real: ")

# Converte os números para reais
num1 = float(num1)
num2 = float(num2)

# Process
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}.")
elif num1 < num2:
    print(f"O número {num2} é maior que o número {num1}.")
else:
    print(f"Os números {num1} e {num2} são iguais.")
