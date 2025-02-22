'''
Exercício Exemplo 2 - Criação e operações com Conjuntos
'''

print(__doc__)

# Criar um conjunto (set)
this_set = {"apple", "banana", "cherry"}
print('this_set=', this_set)


# itens duplicados não são permitidos
this_set = {"apple", "banana", "cherry", "apple"}
print('this_set=', this_set)

# True e 1 é considerado o mesmo valor
this_set = {"apple", "banana", "cherry", True, 1, 2}
print('this_set=', this_set)

# 1 e True é considerado o mesmo valor e é mantido o último
this_set = {"apple", "banana", "cherry", 1, True, 2}
print('this_set=', this_set)

# obter o comprimento de um conjunto
this_set = {"apple", "banana", "cherry"}
print('len(this_set)=', len(this_set))

# Definir itens - Tipos de dados
# Tipos de dados string, int e booleanos:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Um conjunto com strings, iteiros e valores booleanos:
set1 = {"abc", 34, True, 40, "male"}

# type() - Retorna o tipo de dados de um objeto
myset = {"apple", "banana", "cherry"}
print('type(myset)=', type(myset))