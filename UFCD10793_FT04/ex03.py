'''
Exercício 3 - while loop - somas e médias
Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua média.
'''

quantidade = 4
soma = 0
i = 0
while i < quantidade:
    numero = int(input(f'Insira um número inteiro positivo #{i+1}: '))
    soma += numero
    i += 1

print(f'A média dos números é {soma / quantidade}.')