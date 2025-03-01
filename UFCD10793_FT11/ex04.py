'''
Exercício 4 - funções
Escreve uma função em Python que dada uma palavra retorne o número de
vogais nessa palavra.
'''

def conta_vogais(palavra):
    vogais = 'aeiouAEIOU'
    total = 0
    for letra in palavra:
        if letra in vogais:
            total += 1
    return total

# Testes
print('Palavra: "Python" Número de vogais:', conta_vogais('Python')) # 1
print('Palavra: "Universidade" Número de vogais:', conta_vogais('Universidade')) # 6
print('Palavra: "AEIOU" Número de vogais:', conta_vogais('AEIOU')) # 5
print('Palavra: "aeiou" Número de vogais:', conta_vogais('aeiou')) # 5