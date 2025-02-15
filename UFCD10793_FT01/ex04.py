'''
Exercício 4 - calcula o volume de uma esfera

Escreve um programa que calcule o volume de uma esfera. O valor do raio deverá ser
introduzido pelo utilizador (deverá ser criado o ficheiro ex04.py).
'''
from math import pi as PI

raio = float(input('Introduza o raio da esfera: '))
volume = (4/3) * PI * raio**3
print(f'O volume da esfera é {volume:.2f}')
