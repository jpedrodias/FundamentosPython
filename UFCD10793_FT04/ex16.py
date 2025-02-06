'''
Exercício 16 - try except
Escreva um programa que peça ao utilizador números entre 0-10. Se o utilizador inserir um número fora desse intervalo o programa deverá finalizar com uma mensagem personalizada
'''

# Input
numero = int(input('Insira um número entre 0-10: '))
try:
    numero = int(numero)
except ValueError:
    numero = None
    print('O valor inserido não é um número inteiro.')

if numero is not None:
    if numero >= 0 and numero <= 10:
        print('Número inserido:', numero)
    else:
        print('O número inserido não está entre 0-10.')

