'''
Exercício 7 - while loop
Elabora um programa para escrever no ecrã os números de 1 a 100 e os respetivos quadrados
'''

# Input
quantidade = int(input('Quantos números deseja calcular? '))
soma = 0
i = 0
while i < quantidade:
    soma += i 
    i += 1
print(f'A soma dos números de 1 a {quantidade} é {soma}.')