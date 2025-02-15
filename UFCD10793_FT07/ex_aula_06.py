'''
Exercício 6 - Aceder aos itens de uma tupla
• Indexação: primeiro elemento tem índice 0
• Se indicarmos o valor do índice maior que o comprimento de uma tupla, dará
erro. O mesmo quando indicamos um valor não inteiro para o índice.
• Admite indexação negativa.
• Podemos ainda aceder a diversos elementos indicando um intervalo de índices (slicing) – similar às listas.
• também podemos fatiar a tupla usando indexação negativa
'''

tuple1 = ('P', 'Y', 'T' , 'H', 'O', 'N')
for i in range(4):
    print(tuple1[i])


tuple1 = ('P', 'Y' , 'T' , 'H' , 'O', 'N')

# IndexError: tuple index out of range
try:
    print(tuple1[7])
except IndexError as e:
    print(e)


# IndexError: tuple index out of range
# MESMO O ÍNDICE 6 não existe
try:
    print(tuple1[6])
except IndexError as e:
    print(e)


# TypeError: tuple indices must be integers or slices, not float
try:
    print(tuple1[2.0])
except TypeError as e:
    print(e)


tuple1 = ('P', 'Y', 'T', 'H', 'O', 'N')
# Negative indexing
# print last item of a tuple
print(tuple1[-1]) # N
# print second last
print(tuple1[-2]) # 0

# iterate a tuple using negative indexing
for i in range(-6, 0):
    print(tuple1[i], end=", ")
# Output P, Y, T, H, O, N,


tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# slice a tuple with start and end index number
print(tuple1[1:5])
# Output (1, 2, 3, 4)


tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# slice a tuple without start index
print(tuple1[:5])
# Output (0, 1, 2, 3, 4)

# slice a tuple without end index
print(tuple1[6:])
# Output (6, 7, 8, 9, 10)

tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# slice a tuple using negative indexing
print(tuple1[-5 :- 1])
# Output (6, 7, 8, 9)