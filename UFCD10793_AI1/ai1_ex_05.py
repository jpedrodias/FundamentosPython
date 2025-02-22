'''
Avaliação Intermédia 1 - Exercício 5

Elabora uma script em python que peça ao utilizador um número e some todos os números de 1 até esse mesmo número. Deves utilizar o tratamento de erros.
'''

from ai1_mytools import better_input

print(__doc__)

# Etapa 1: Pedir ao utilizador um número inteiro superior a zero
a = better_input("Digite um número inteiro superior a zero: ", 'Erro: Apenas números inteiros superiores a zero são permitidos.', not_allowed={0})

# Etapa 2: Somar todos os números de 1 até esse mesmo número
soma = 0
for i in range(1, a + 1):
    soma += i

# Etapa 3: Apresentar o resultado
print('A soma dos números de 1 até', a, 'é', soma)