'''
Exercício 2 - funções
Escreve uma função em Python que, dados a medida do comprimento do lado de
um quadrado imprima os valores do seu perímero e da sua área (area=lado x
lado; perimetro = 4 x lado).
'''

def quadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    print('Quadrado com lado', lado)
    print(' * Área:', area)
    print(' * Perímetro:', perimetro)

# Testes
quadrado(1) # Área: 1 Perímetro: 4
quadrado(2) # Área: 4 Perímetro: 8
quadrado(3) # Área: 9 Perímetro: 12
quadrado(4) # Área: 16 Perímetro: 16