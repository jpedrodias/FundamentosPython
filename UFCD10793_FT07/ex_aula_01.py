'''
Exercício 1 - Tuplas
 Criação e Manipulação de Tuplas

Reproduz os seguintes exemplos. O objetivo é instanciar tuplas e aplicar as operações específicas deste tipo de dados

Criar e imprimir tuplas. Para criarmos tuplas podemos usar () ou o construtor tuple(). Uma tupla pode ter diferentes tipos de dados.
'''

# create a tuple using ()
# number tuple
number_tuple = (10, 20, 25.75)
print(number_tuple)
# Output (10, 20, 25.75)

# string tuple
string_tuple = ('Jessa', 'Emma' , 'Kelly' )
print(string_tuple)
# Output ('Jessa', 'Emma' , 'Kelly' )

# mixed type tuple
sample_tuple = ('Jessa', 30, 45.75, [25, 78])
print(sample_tuple)
# Output ('Jessa', 30, 45.75, [25, 78])

# create a tuple using tuple() constructor
sample_tuple2 = tuple(('Jessa', 30, 45.75, [23, 78]))
print(sample_tuple2)
# Output ('Jessa', 30, 45.75, [23, 78])