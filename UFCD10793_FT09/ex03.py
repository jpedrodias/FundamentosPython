'''
Exercício 3 - dicionários

Efetua um programa em python:

a. Instancie o seguinte dicionário:
computadores_1 = {
 "Marca":"Asus",
 "Ecra":"14Pol",
 "RAM": [4, 8, 12]
}

b. Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]
c. Permita ao utilizador introduzir um valor específico de RAM e verificar se esta está presente na lista.
d. Acrecente 16 como novo valor de RAM.
e. Copie o dicionário para um novo usando Deep Copy().
f. Na lista nova modifique a marca para “Lenovo” e os valores da RAM para [4,8]. Imprima a nova lista
g. Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]- Imprima a respetiva lista
h. Cria uma lista cujos elementos são os três dicionários.
i. Imprima as marcas com 128G de RAM
j. Imprima as marcas com 8 e 12 de RAM
'''

# a. Instanção do dicionário:
computadores_1 = {
    "Marca": "Asus",
    "Ecra": "14Pol",
    "RAM": [4, 8, 12]
}

# b. Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]
computadores_1["Disco"] = ["128G", "256G"]

# c. Permita ao utilizador introduzir um valor específico de RAM e verificar se esta está presente na lista.
ram = int(input('Introduza um valor de RAM: '))
if ram in computadores_1.get("RAM", []): # uso da função get() para evitar erro de chave inexistente
    print('RAM presente na lista')
else:
    print('RAM não presente na lista')

# d. Acrecente 16 como novo valor de RAM.
if "RAM" not in computadores_1:
    computadores_1["RAM"] = []

if 16 not in computadores_1["RAM"]:
    computadores_1["RAM"].append(16)

# e. Copie o dicionário para um novo usando Deep Copy().
computadores_2 = computadores_1.copy()

# f. Na lista nova modifique a marca para “Lenovo” e os valores da RAM para [4,8]. Imprima a nova lista
computadores_2["Marca"] = "Lenovo"
computadores_2["RAM"] = [4, 8]
print('Computadores 2:', computadores_2)


# g. Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]- Imprima a respetiva lista
computadores_3 = computadores_1.copy()
computadores_3["Marca"] = "HP"
computadores_3["Disco"] = ["256G"]
print('Computadores 3:', computadores_3)

# h. Cria uma lista cujos elementos são os três dicionários.
computadores = [computadores_1, computadores_2, computadores_3]

# i. Imprima as marcas com 128G de RAM
for computador in computadores:
    if "Disco" in computador and "128G" in computador["Disco"]:
        print('Marca com 128G de RAM:', computador["Marca"])


# j. Imprima as marcas com 8 e 12 de RAM
for computador in computadores:
    if "RAM" in computador and 8 in computador["RAM"] and 12 in computador["RAM"]:
        print('Marca com 8 e 12 de RAM:', computador["Marca"])

# k. Imprima todos dicionários que se chamem computadores
for name, objeto in locals().copy().items():
    if isinstance(objeto, dict) and name.startswith('computadores'):
        print(name, objeto)