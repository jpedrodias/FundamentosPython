'''
Exercício 3 - função sum (soma)

Escreve um programa em python que solicite três números inteiros ao utilizador e imprima a soma dos mesmos.
'''

num1 = input('Insere o número 1 (em interiro): ')
num2 = input('Insere o número 2 (em interiro): ')
num3 = input('Insere o número 3 (em interiro): ')

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

numeros = [num1, num2, num3]


#soma = num1 + num2 + num3
soma = sum(numeros)

print(f'A soma dos {len(numeros)} é {soma}')
