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
dicionario = {chave.upper(): valor.strip() if isinstance(valor, str) else valor for chave, valor in dicionario.items()}

print('Dicionário:', dicionario)