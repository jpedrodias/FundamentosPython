'''
Exercício 9 - Adicionar e alterar itens numa tupla
Uma lista é um tipo mutável, o que significa que podemos adicionar ou modificar
valores, mas as tuplas são imutáveis, portanto, não podem ser alteradas. Além disso,
como uma tupla é imutável, não há métodos internos para adicionar itens à tupla. Se
tentarmos modificar algum valor obteremos um erro
'''

tuple1 = (0, 1, 2, 3, 4, 5)
try:
    tuple1[1] = 10
except TypeError as e:
    print(e)
    # Output TypeError: 'tuple' object does not support item assignment

'''
Como solução alternativa, podemos converter a tupla numa lista, adicionar itens e
convertê-la novamente como tupla. 
'''
tuple1 = (0, 1, 2, 3, 4, 5)

# converting tuple into a list
sample_list = list(tuple1)
# add item to list
sample_list.append(6)

# converting list back into a tuple
tuple1 = tuple(sample_list)
print(tuple1)
# Output (0, 1, 2, 3, 4, 5, 6)