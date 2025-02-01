'''
Exercício 4 - função len (tamanho)
Escreve um programa que solicite duas notas ([nota1] e [nota2]) ao utilizador e apresente a média das mesmas da seguinte forma
'''

# Solicitar as notas ao utilizador
nota1 = input('Insere a nota 1 (em inteiro): ')
nota2 = input('Insere a nota 2 (em inteiro): ')

# Converter as notas para inteiros
nota1 = int(nota1)
nota2 = int(nota2)

# Cria uma coleção com as notas: uma lista
notas = [nota1, nota2]

# Calcular a média das notas usando a função sum() e len()
media = sum(notas) / len(notas)

# Arredondar a média para 2 casas decimais
media = round(media, 2)

# Apresentar a média das notas
print(f'A média das notas {nota1} e {nota2} é {media}')