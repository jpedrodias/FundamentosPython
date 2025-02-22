'''
Avaliação Intermédia 1 - Exercício 2

Peça dois números ao utilizador e trate a divisão por zero.
'''

def better_input(prompt, error_message="Erro! Introduza um número inteiro.", data_type=int, not_allowed={}):
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


# Exemplo 1
try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    print("Resultado da divisão:", a / b)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Apenas números inteiros são permitidos.")


# Exemplo 2
a = better_input("Digite o numerador: ", 'Erro: Apenas números inteiros são permitidos.')
b = better_input("Digite o denominador: ", error_message="Erro: Apenas números inteiros diferentes de zero são permitidos.", not_allowed={0})
print("Resultado da divisão:", a / b)