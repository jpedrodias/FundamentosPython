'''
Avaliação Intermédia 1 - Exercício 5

Elabora uma script em python que peça ao utilizador um número e some todos os números de 1 até esse mesmo número. Deves utilizar o tratamento de erros.
'''

def better_input(prompt, error_message="Erro! Introduza um número inteiro superior a zero.", data_type=int, not_allowed={}):
    done = False
    while not done:
        user_input = input(prompt)
        data = None
        try:
            data = data_type(user_input)
            done = True
        except ValueError:
            print(error_message)
        
        if data in not_allowed:
            print(error_message)
            done = False
    
    return data


print(__doc__)

# Etapa 1: Pedir ao utilizador um número inteiro superior a zero
a = better_input("Digite um número inteiro superior a zero: ", 'Erro: Apenas números inteiros superiores a zero são permitidos.', not_allowed={0})

# Etapa 2: Somar todos os números de 1 até esse mesmo número
soma = 0
for i in range(1, a + 1):
    soma += i

# Etapa 3: Apresentar o resultado
print('A soma dos números de 1 até', a, 'é', soma)