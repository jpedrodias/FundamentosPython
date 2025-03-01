'''
Exercício 4 - listas
Considera a seguinte lista:
    nums = [10, 2.5, 7, 11, 7.9, 'Python', True, 6, 5.8, 'Listas']

Efetua um programa em python que:
a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros
'''

nums = [10, 2.5, 7, 11, 7.9, 'Python', True, 6, 5.8, 'Listas']

# a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
inteiros = 0
floats = 0
strings = 0
boleanos = 0

# Usando for loop & type
for num in nums:
    if type(num) == int:
        inteiros += 1
    elif type(num) == float:
        floats += 1
    elif type(num) == str:
        strings += 1
    elif type(num) == bool:
        boleanos += 1

# (EXTRA) Usando list comprehension
inteiros = len([ num for num in nums if type(num) == int   ])
floats   = len([ num for num in nums if type(num) == float ])
strings  = len([ num for num in nums if type(num) == str   ])
boleanos = len([ num for num in nums if type(num) == bool  ])

# (EXTRA) Usando list comprehension e sum
inteiros = sum( 1 for num in nums if type(num) == int   )
floats   = sum( 1 for num in nums if type(num) == float )
strings  = sum( 1 for num in nums if type(num) == str   )
boleanos = sum( 1 for num in nums if type(num) == bool  )


print(f'Quantidade de inteiros: {inteiros}')
print(f'Quantidade de floats: {floats}')
print(f'Quantidade de strings: {strings}')
print(f'Quantidade de boleanos: {boleanos}')


# b. Efetua a média de todos os valores inteiros na lista.
soma = 0
contador = 0
for num in nums:
    if type(num) == int:
        soma += num
        contador += 1

media = soma / contador
print(f'Média dos valores inteiros: {media}')

# c. Crie e retorne uma nova lista só com os valores inteiros
inteiros = [num for num in nums if type(num) == int]
print(f'Lista só com os valores inteiros: {inteiros}')

# End of UFCD10793_FT06/ex_aula_04.py