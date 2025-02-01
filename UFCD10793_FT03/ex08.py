'''
Exercício 8 - Classificação de Triângulos
Escreve um programa para classificar um triângulo de acordo com o comprimento dos 
seus lados. Considere as seguintes informações: 
• Triângulo equilátero: todos os lados possuem o mesmo comprimento; 
• Triângulo escaleno: todos os lados possuem comprimento diferente; 
• Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento.

'''


# Input
lado1 = input("Insira o comprimento do lado 1: ")
lado2 = input("Insira o comprimento do lado 2: ")
lado3 = input("Insira o comprimento do lado 3: ")

# Converte os números para reais
lado1 = float(lado1)
lado2 = float(lado2)
lado3 = float(lado3)

# Process
if lado1 == lado2 == lado3:
    print(f"O triângulo é equilátero.")
elif lado1 != lado2 != lado3:
    print(f"O triângulo é escaleno.")
else:
    print(f"O triângulo é isósceles.")
