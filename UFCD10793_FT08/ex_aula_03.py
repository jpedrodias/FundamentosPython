'''
Exercício Exemplo 3 - Construtor set
Usando o construtor set() para criar um conjunto:
'''

print(__doc__)

this_set = set(("apple", "banana", "cherry")) # note the double round-brackets
print(this_set)

# métodos e operações com conjuntos

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

#itens duplicados são removidos
numbers = {2, 4, 6, 6, 2, 8}
print(numbers) # {8, 2, 4, 6}
