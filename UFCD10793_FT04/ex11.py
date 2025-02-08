'''
Exercício 11 - while loop - somatório e produtório
Escreve um programa que calcule a soma e o produto dos N primeiros números naturais.
'''

# Input
quantidade = int(input('Quantos números deseja calcular? '))
soma = 0
produto = 1
i = 1
while i < quantidade:
    soma += i
    produto *= i
    i += 1
print(f'A soma dos números de 1 a {quantidade} é {soma} e o produto é {produto}.')
