'''
Exercício 1 - dicionários

Considere o seguinte dicionário, a que cada prato é associado o respectivo valor em euros:

menu = {
    "entremeada": 7,
    "Sardinhas": 6,
    "Filetes": 5.5,
    "Prego": 7,
    "Hamburger": 5.5 
}

Efetua um programa em python que, após instalar a variável:
a. Devolva o preço do "prego".
b. Faça o print de todas as chaves do dicionário
c. Acrescente na lista “omolete” com o preço de 5
d. Faça o print de todo o dicionário, para visualizar as alterações.
'''



menu = {
    "entremeada": 7,
    "Sardinhas": 6,
    "Filetes": 5.5,
    "Prego": 7,
    "Hamburger": 5.5 
}

# a. Devolva o preço do "prego".
print('Valor do prego é', menu["Prego"])

# b. Faça o print de todas as chaves do dicionário
print('Chaves do dicionário:', ", ".join(menu.keys()))


# c. Acrescente na lista “omolete” com o preço de 5
menu["omolete"] = 5

# d. Faça o print de todo o dicionário, para visualizar as alterações.
print('Chaves e Valores do dicionário:')
for chave, valor in menu.items():
    print(f' * {chave} - {valor:.2f}€')
print()

