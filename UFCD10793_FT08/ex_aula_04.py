'''
Exercício Exemplo 4 - adicionar e atualizar elementos
'''
print(__doc__)

numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
#Conjuntos são mutáveis. No entanto, como não estão ordenados, a indexação não tem significado.
#Não podemos aceder ou alterar um elemento de um conjunto usando indexação ou divisão. o tipo de dados definido não é compatível.

numbers.add(32)

print('Updated Set:', numbers)