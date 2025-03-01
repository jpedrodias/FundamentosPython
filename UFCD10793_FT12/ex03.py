'''
Exercício 3 - Bloco try/exception ValueError
Escreva um programa Python que solicita que o usuário insira um inteiro e gera uma
exceção ValueError se a entrada não for um inteiro válido.
'''

def get_integer_input(prompt):
    try:
        value = int(input(prompt))
    except ValueError:
        value = None
        print("Error: Invalid input, input a valid integer.")
    return value

# Usage
n = get_integer_input("Input an integer: ")
print("Input value:", n)