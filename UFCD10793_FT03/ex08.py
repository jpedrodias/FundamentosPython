'''
Exercício 8 - Classificação de Triângulos
Escreve um programa para classificar um triângulo de acordo com o comprimento dos 
seus lados. Considere as seguintes informações: 
• Triângulo equilátero: todos os lados possuem o mesmo comprimento; 
• Triângulo escaleno: todos os lados possuem comprimento diferente;
• Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento.
'''


# Input
lado_a = input("Insira o comprimento do lado a: ")
lado_b = input("Insira o comprimento do lado b: ")
lado_c = input("Insira o comprimento do lado c: ")

# Converte os números para reais
lado_a = float(lado_a)
lado_b = float(lado_b)
lado_c = float(lado_c)

# Process
if lado_a == lado_b == lado_c:
    print(f"O triângulo é equilátero.")
elif lado_a != lado_b != lado_c:
    print(f"O triângulo é escaleno.")
else:
    print(f"O triângulo é isósceles.")
