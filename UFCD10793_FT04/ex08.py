'''
Exercício 8 - while loop
Elabora um programa para escrever no ecrã os números de 1 a 100 e os respetivos quadrados
'''

# Input

numero = int(input('Tabuada do número? '))
quantidade = 10
i = 0
while i < quantidade:
    print(f'{numero} x {i+1} = {numero * (i+1)}')    
    i += 1
