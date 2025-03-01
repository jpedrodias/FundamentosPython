'''
Exercício 4 - Strings

Escreve um programa em Python que
Escreve um programa em Python que
a. Imprima o texto anterior todo em maiúsculas;
b. Peça uma palavra ao utilizador e verifique se a mesma está ou não no
texto, devolvendo o resultado ao utilizador.
c. Imprima o número de vezes que a letra "O" ocorre no texto
d. Substitua todaa as ocorrências da letra "P" no texto por "_"
'''


txt = '''Python é uma linguagem de programação
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte.'''

# a. Imprima o texto anterior todo em maiúsculas;
print('a)', txt.upper())

# b. Peça uma palavra ao utilizador e verifique se a mesma está ou não no texto, devolvendo o resultado ao utilizador.
palavra = input('b) Insira uma palavra: ')
if palavra.lower() in txt.lower():
    print('A palavra está no texto')
else:
    print('A palavra não está no texto')

# c. Imprima o número de vezes que a letra "O" ocorre no texto
print('c)', txt.upper().count('O'))

# d. Substitua todaa as ocorrências da letra "P" no texto por "_"
new_txt = txt.replace('P', '_')
print('d)', new_txt)
