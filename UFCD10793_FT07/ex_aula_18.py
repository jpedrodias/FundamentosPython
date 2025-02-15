'''
Exercício 18 - função interna: any
Pelo menos um valor verdadeiro. Retorna falso quando todos os valores são falso e a tupla está vazia.
'''

# any() with All True values
tuple1 = (1, 1, True)
print(any(tuple1)) # True

# any() with One false value
tuple2 = (0, 1, True, 1)
print(any(tuple2)) # True

# any() with all false values
tuple3 = (0, 0, False)
print(any(tuple3)) # False

# any() with Empty tuple
tuple4 = ()
print(any(tuple4)) # False