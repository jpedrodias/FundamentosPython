'''
Exercício 3 - função sum (soma)

Escreve um programa em python que solicite três números inteiros ao utilizador e imprima a soma dos mesmos.
'''

# Solicitar 3 números inteiros ao utilizador
num1 = input('Insere o número 1 (em interiro): ')
num2 = input('Insere o número 2 (em interiro): ')
num3 = input('Insere o número 3 (em interiro): ')

# Converter os números para inteiros
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Criar uma lista com os números
numeros = [num1, num2, num3]


# Calcular a soma dos números
soma = sum(numeros)

# Imprimir a soma dos números
print(f'A soma dos {len(numeros)} é {soma}')