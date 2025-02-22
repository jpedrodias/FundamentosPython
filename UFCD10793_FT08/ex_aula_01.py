'''
Exercício Exemplo 1 - Criação e operações com Conjuntos
Criação e Manipulação de Conjuntos

Operações de conjuntos em Python. Conjuntos são coleções não ordenadas de elementos únicos. Podemos criar conjuntos usando {} ou o construtor set(). 
Conjuntos não suportam indexação, slicing ou qualquer operação que dependa da ordem dos elementos. Conjuntos são úteis para remover duplicatas de uma lista e realizar 
operações matemáticas como união, interseção, diferença e diferença simétrica.

* Subtração: a - b
* União: a | b
* Interseção: a & b
* Diferença simétrica: a ^ b

'''

print(__doc__)

xs = {1, 2, 3}
aux = 1 in xs # True, implementação mais eficiente
print(aux)

a = set('abracadabra') # a = {'a', 'r', 'b', 'c', 'd'}
print(a) 

b = set('alacazam') # b = {'a', 'l', 'm', 'c', 'z'}
print(b)

# SUBTRACTION
c = a - b # c = {'r', 'd', 'b'}, letras em a mas não em b
print(c)

# OR
c = a | b # c = {'a', 'r', 'b', 'c', 'd', 'l', 'm', 'z'}, letras em a ou em b, ou seja, em ambos
print(c)

# AND
c = a & b # c = {'a', 'c'}, letras tanto em a quanto em b
print(c)

# XOR
c = a ^ b # c = {'r', 'd', 'b', 'l', 'm', 'z'}, letras em a ou em b, mas não em ambos
print(c)
