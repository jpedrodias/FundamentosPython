'''
Exercício 9 - Índice de Massa Corporal (IMC)
O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa. 
Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que, de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de acordo com as seguintes condições: 
• IMC<17 - Muito abaixo do peso ideal 
• 17<=IMC<18,5 - Abaixo do peso 
• 18,5<=IMC<25 - Peso normal 
• 25<=IMC<30 - Acima do peso 
• 30<=IMC<35 - Obesidade I 
• 35<=IMC<40 - Obesidade II (severa) 
• IMC>=40 - Obesidade III (mórbida)

Nota: IMC=massa/(altura*altura)

'''

# Input
nome = input("Insira o seu nome: ")
idade = input("Insira a sua idade: ")
peso = input("Insira o seu peso (kg): ")
altura = input("Insira a sua altura (m): ")

# Converte os números para reais
idade = int(idade)
peso = float(peso)
altura = float(altura)

# Process
imc = peso/(altura*altura)
img = round(imc, 2)

if img < 17:
    print(f"O IMC de {nome} é {img} e está muito abaixo do peso ideal.")
elif 17 <= img < 18.5:
    print(f"O IMC de {nome} é {img} e está abaixo do peso.")
elif 18.5 <= img < 25:
    print(f"O IMC de {nome} é {img} e está com o peso normal.")
elif 25 <= img < 30:
    print(f"O IMC de {nome} é {img} e está acima do peso.")
elif 30 <= img < 35:
    print(f"O IMC de {nome} é {img} e está com obesidade I.")
elif 35 <= img < 40:
    print(f"O IMC de {nome} é {img} e está com obesidade II (severa).")
else:
    print(f"O IMC de {nome} é {img} e está com obesidade III (mórbida).")
