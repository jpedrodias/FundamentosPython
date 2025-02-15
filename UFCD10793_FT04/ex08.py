'''
Exercício 8 - while loop - tabuada do 5
Escreve um programa que coloque no ecrã a tabuada do número 5.
'''

#numero = int(input('Tabuada do número? '))
numero = 5
quantidade = 10
i = 0
while i < quantidade:
    print(f'{numero} x {i+1} = {numero * (i+1)}')    
    i += 1