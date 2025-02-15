'''
Exercício 16 - funções internas max e min
Funções internas: max(), min(). Estas funções não podem ser aplicadas em tuplas com tipos de dados heterógeneos
'''

tuple1 = ('xyz', 'zara', 'abc')
# The Maximum value in a string tuple
print(max(tuple1))
# Output zara

# The minimum value in a string tuple
print(min(tuple1))
# Output abc

tuple2 = (11, 22, 10, 4)
# The Maximum value in a integer tuple
print(max(tuple2))
# Output 22
# The minimum value in a integer tuple
print(min(tuple2))
# Output 4

tuple3 = ('a', 'e', 11, 22, 15)
# max item
print(max(tuple3))