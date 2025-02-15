'''
Exercício 12 - Cópia de uma tupla
'''

tuple1 = (0, 1, 2, 3, 4, 5)

# copy tuple
tuple2 = tuple1
print(tuple2)
# Output (0, 1, 2, 3, 4, 5)

# changing tuple2
# converting it into a list
sample_list = list(tuple2)
sample_list.append(6)

# converting list back into a tuple2
tuple2 = tuple(sample_list)

# printing the two tuples
print(tuple1)
# Output (0, 1, 2, 3, 4, 5)
print(tuple2)
# Output (0, 1, 2, 3, 4, 5, 6)