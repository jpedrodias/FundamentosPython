'''
Avaliação Intermédia 1 - Exercício 1 (b)

Escreva um programa que pede ao utilizador um número inteiro e trata erros de entrada.
'''

def better_input(prompt, error_message="Erro! Introduza um número inteiro.", data_type=int):
    done = False
    while not done:
        user_input = input(prompt)
        try:
            data = data_type(user_input)
            done = True
        except ValueError:
            print(error_message)
    
    return data

number = better_input("Introduza um número inteiro: ")