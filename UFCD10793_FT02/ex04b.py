'''
Exercício 4 - função len (versão mais completa)
Escreve um programa que solicite duas notas ([nota1] e [nota2]) ao utilizador e apresente a média das mesmas da seguinte forma.

"A média das notas [nota1] e [nota2] é [média]."
'''

# Solicitar as notas ao utilizador
notas = []
nota = ''
while nota is not None:
    msg = f'Insere a nota {len(notas) + 1 } (em inteiro): '
    nota = input(msg)
    try:
        nota = int(nota)
    except ValueError:
        nota = None
    
    if nota:
        notas.append(nota)


# DEBUG: Apenas para efeitos de debug - apresenta o número de notas inseridas
print(f'Inseridas {len(notas)} notas')

# Calcular a média das notas
media = sum(notas) / len(notas)

# Arredondar a média a duas casas decimais
media = round(media, 2)

# Apresentar a média das notas
print(f'A média das notas é {media}')