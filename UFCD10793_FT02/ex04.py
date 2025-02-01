'''
Escreve um programa que solicite duas notas ([nota1] e [nota2]) ao utilizador e apresente a média das mesmas da seguinte forma
'''

nota1 = input('Insere a nota 1 (em inteiro): ')
nota2 = input('Insere a nota 2 (em inteiro): ')

nota1 = int(nota1)
nota2 = int(nota2)

notas = [nota1, nota2]


#soma = num1 + num2 + num3
soma = sum(notas)
media = soma / len(notas)

media = round(media, 2)

print(f'A média das notas {nota1} e {nota2} é {media}')