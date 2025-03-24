'''
Avaliação Intermédia 1 - Parte 1 - Exercício 2

Peça dois números ao utilizador e trate a divisão por zero.
'''

try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    print("Resultado da divisão:", a / b)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Apenas números inteiros são permitidos.")

