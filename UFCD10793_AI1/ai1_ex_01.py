'''
Avaliação Intermédia 1 - Exercício 1

Escreva um programa que pede ao utilizador um número inteiro e trata erros de entrada.
'''

def my_imput(prompt, error_message="Erro! Introduza um número inteiro.", ):
    done = False
    while not done:
        user_imput = input(prompt)