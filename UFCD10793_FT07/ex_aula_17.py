'''
Exercício 17 - função interna: all
Função all() – verdadeiro se todos os valores verdadeiros e no caso de tupla vazia.
Falso nos restantes casos
'''

# all() with All True values
tuple1 = (1, 1, True)
print(all(tuple1)) # True

# all() All True values
tuple1 = (1, 1, True)
print(all(tuple1)) # True

# all() with One false value
tuple2 = (0, 1, True, 1)
print(all(tuple2)) # False

# all() with all false values
tuple3 = (0, 0, False)
print(all(tuple3)) # False

# all() Empty tuple
tuple4 = ()
print(all(tuple4)) # True