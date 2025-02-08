'''
Exercício 4 - while loop - 100 vezes
Escreve um programa para escrever no ecrã a palavra olá 100 vezes.
'''
# em python como fazer clear do terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')


quantidade = 100
palavra = 'olá'
i = 0
while i < quantidade:
    print(palavra, end=' ')
    i += 1
    if i % 20 == 0: print()
print()