'''
Exercício 2 - FAV Enunciado Geral

Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa palavra. 
'''

# Versão sem usar a função count
def contar_vogais(palavra):
    '''Conta o número de vogais numa palavra'''
    vogais = 'aeiouAEIOU'
    return sum(1 for letra in palavra if letra in vogais)


palavra = input('Digite uma palavra: ')
numero_de_vogais = contar_vogais(palavra)

print(f'(ver1) A palavra {palavra} tem {numero_de_vogais} vogais.')


# Versão usando a função count
def contar_vogais(palavra):
    '''Conta o número de vogais numa palavra'''
    vogais = 'aeiouAEIOU'
    return sum(palavra.count(letra) for letra in vogais)

print(f'(ver2) A palavra {palavra} tem {numero_de_vogais} vogais.')


# Versão usando modulos: re (Regular Expresstions)
def contar_vogais(palavra):
    '''Conta o número de vogais numa palavra'''
    import re
    padrao = r'[aeiou]'
    return len(re.findall(padrao, palavra, re.IGNORECASE))

print(f'(ver3) A palavra {palavra} tem {numero_de_vogais} vogais.')
