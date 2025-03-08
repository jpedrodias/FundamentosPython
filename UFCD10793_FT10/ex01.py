'''
Exercício 1 - Strings strip, slice e upper
'''


txt =" uFcd - proGRAMação eM pyTHON "

#Imprimir texto
print(txt)

#Imprimir Texto sem espaçamento inicial
txt=txt.strip()
print(txt)

#Imprimir frase até à palavra na 13ª posição
print(txt[:13])

# Imprimir frase a partir da palavra na 13ª posição
print(txt[-5:])

# Imprimir frase em maiúsculas
txt = txt.upper()
print(txt)

# Formatação de strings
nome = "Sandra Oliveira"
print(f"O {nome} gosta muito da {txt}.")