'''
Exercício 7 - while loop - soma dos N primeiros números naturais
Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N)
em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito
utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não
sabíamos a fórmula).
'''

quantidade = int(input('Quantos números deseja calcular? '))
soma = 0
i = 0
while i < quantidade:
    soma += i 
    i += 1
print(f'A soma dos números de 1 a {quantidade} é {soma}.')