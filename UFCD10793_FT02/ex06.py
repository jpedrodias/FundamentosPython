'''
Exercício 6 - função conversão temperaturas
Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a converta para grau Celsius (C), devolvendo o resultado da conversão.
'''

# Solicitar a temperatura em Fahrenheit
fahrenheit = input('Insere a temperatura em Fahrenheit: ')

# Converter a temperatura para float
fahrenheit = float(fahrenheit)

# Calcular a temperatura em graus Celsius
celsius = (fahrenheit - 32) * 5.0/9.0

# Arredondar a temperatura para 2 casas decimais
celsius = round(celsius, 2)

# Apresentar a temperatura em graus Celsius
print(f'A temperatura em graus Celsius é {celsius}')