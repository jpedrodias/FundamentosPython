'''
Exercício 6 - função conversão temperaturas
Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a converta para grau Celsius (C), devolvendo o resultado da conversão.
'''

fahrenheit = input('Insere a temperatura em Fahrenheit: ')

fahrenheit = float(fahrenheit)

celsius = (fahrenheit - 32) * 5.0/9.0

celsius = round(celsius, 2)

print(f'A temperatura em graus Celsius é {celsius}')
