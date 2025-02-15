'''
Exercício 3 - Embalar e desembalar dados
Em Python, podemos criar uma tupla empacotando um grupo de variáveis. O
empacotamento pode ser usado quando queremos agrupar vários valores num única
variável. Geralmente, essa operação é chamada de empacotamento de tuplas. Da
mesma forma, podemos descompactar os itens apenas atribuindo os itens da tupla ao
mesmo número de variáveis. Esse processo é chamado de “Descompactação”
'''

# packing variables into tuple
tuple1 = 1, 2, "Hello"
# display tuple
print(tuple1)
# Output (1, 2, 'Hello')

print(type(tuple1))

# Output class 'tuple

# unpacking tuple into variable
i, j, k = tuple1
# printing the variables
print(i, j, k)
# Output 1 2 Hello