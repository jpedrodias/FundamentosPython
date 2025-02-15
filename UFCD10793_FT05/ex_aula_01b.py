'''
Exercício 1b - tabuada com ciclo for e while
Utilizando estruturas de repetição escreva um programa que mostre os
resultados da tabuada de multiplicação dos números entre 1 e 10, como segue.
'''


print('Solução 1: ')
for valor in range(1,11):
    for numero in range(1,11):
        print(f'{valor} x {numero} = {valor*numero}')



print('Solução 2: ')
x = 1
while x <= 10:
    y = 1
    while y <= 10:
        print(f'{x} x {y} = {x*y}')
        y+=1
    x+=1