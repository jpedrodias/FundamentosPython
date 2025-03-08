'''
Exercício 2 - Manipulação de dicionários

Efetua um programa em python onde:
a. Cries um dicionário e efetues o respetivo print.
b. Acrescentes dois novos elementos ao dicionário.
c. Removes um dos elementos da lista;
d. Efetues uma operação, à escolha, sobre os dados no dicionário
'''

# a. Cries um dicionário e efetues o respetivo print.
dicionario = {
    "nome": "João",
    "idade": 25,
    "curso": "Informática"
}

print('Dicionário:', dicionario)

# b. Acrescentes dois novos elementos ao dicionário.
dicionario["morada"] = "     Rua das Flores      "
dicionario["telefone"] = 912345678

# c. Removes um dos elementos da lista;
dicionario.pop("idade")

# d. Efetues uma operação, à escolha, sobre os dados no dicionário
# manipulação em simultâneo das chaves e dos valores (mantem tudo o que não é string)


dicionario = {}
for chave, valor in dicionario.items():
    if isinstance(valor, str):
        dicionario[chave.upper()] = valor.strip()
    else:
        dicionario[chave.upper()] = valor


# EQUIVALENTE USANDO COMPREHENSION
dicionario = {chave.upper(): valor.strip() if isinstance(valor, str) else valor for chave, valor in dicionario.items()}

# EXPLICAÇÃO:
# Nível 1: loop for que percorre o dicionário
#     for chave, valor in dicionario.items():
#          ...
#
# Nível 2: bloco if que verifica se o valor é uma string
#     if isinstance(valor, str)
# 
# se true devolve a string limpa (sem espaços à esquerda e à direita)
#
# Nível 3: devolve chave : valor


print('Dicionário:', dicionario)