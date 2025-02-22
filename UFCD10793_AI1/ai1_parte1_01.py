'''
Avaliação Intermédia 1 - Parte 1 - Exercício 1

Escreva um programa que pede ao utilizador um número inteiro e trata erros de entrada.
'''

try:
    numero = int(input("Digite um número inteiro: "))
    print("Número inserido:", numero)
except ValueError:
    print("Erro: O valor deve ser um número inteiro.")
