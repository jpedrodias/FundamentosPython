'''
Exercício 7 - Encontrar items método index
Podemos procurar um determinado item na tupla usando o método index(). O mesmo retornará a posição desse item.
O método index() aceita três argumentos:
item – O item que precisa ser pesquisado
start – (Opcional) - O valor inicial do índice a partir do qual a pesquisa será iniciada
end – (Opcional) - O valor final do indíce da pesquisa
'''

tuple1 = (10, 20, 30, 40, 50)

# get index of item 30
position = tuple1.index(30)
print(position)
# Output 2


tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
# Limit the search locations using start and end
# search only from location 4 to 6
# start = 4 and end = 6
# get index of item 60
position = tuple1.index(60, 4, 6)
print(position)
# Output 5

tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
#index out of range
position = tuple1.index(10)
print(position)

# position = tuple1.index(10, 1)
# Output ValueError: tuple.index(x): x not in tuple