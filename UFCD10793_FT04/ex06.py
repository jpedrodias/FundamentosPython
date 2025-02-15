'''
Exercício 6 - while loop - números e quadrados
Elabora um programa para escrever no ecrã os números de 1 a 100 e os respetivos quadrados
'''

quantidade = 100
i = 0
while i < quantidade:
    quadrado = (i+1) ** 2
    print(f'O quadrado de {i+1} é { quadrado }.')
    i += 1
print()
