'''
Exercício 9 - while loop - tabuada
Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número introduzido pelo utilizador.
'''

numero = int(input('Tabuada do número? '))
#numero = 5
quantidade = 10
i = 0
while i < quantidade:
    print(f'{numero} x {i+1} = {numero * (i+1)}')    
    i += 1
