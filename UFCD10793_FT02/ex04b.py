'''
Escreve um programa que solicite duas notas ([nota1] e [nota2]) ao utilizador e apresente a média das mesmas da seguinte forma
'''

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

print(f'Inseridas {len(notas)} notas')

soma = sum(notas)
media = soma / len(notas)

media = round(media, 2)

print(f'A média das notas é {media}')