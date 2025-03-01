'''
Exercício 2 - Bloco try/exception ZeroDivisionError
Escreva um programa Python para manipular uma exceção ZeroDivisionError ao dividir um
número por zero.
'''

def divide_numbers(x, y):
    try:
        result = x / y
        print("Result:", result)

    except ZeroDivisionError:
        print("The division by zero operation is not allowed.")

numerator = 100
denominator = 0
divide_numbers(numerator, denominator)
