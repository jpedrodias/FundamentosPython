'''
Exercício 5 - Bloco try/exception TypeError
Escreva um programa Python que solicita ao utilizador dois números e gera uma exceção
TypeError se as entradas não forem numéricas.
'''

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")

# Usage
n1 = get_numeric_input("Input the first number: ")
n2 = get_numeric_input("Input the second number: ")
result = n1 * n2
print("Product of the said two numbers:", result)