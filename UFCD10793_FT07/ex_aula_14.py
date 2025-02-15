'''
Exercício 14 - Concatenar(juntar) duas tuplas – usar a função soma
'''

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

# using sum function
tuple3 = sum((tuple1, tuple2),())
print(tuple3)
# Output (1, 2, 3, 4, 5, 3, 4, 5, 6, 7)