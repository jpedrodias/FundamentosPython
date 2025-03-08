'''
Exercício 1 - funções
Escreve uma função em Python que, dados a medida do comprimento dos três
lados de um triângulo diga se o mesmo é equilátero, isósceles ou escaleno.
'''

def tipo_triangulo(a,b,c):
    if a==b==c:
        return "Equilátero"
    elif a==b or a==c or b==c:
        return "Isósceles"
    else:
        return "Escaleno"
    

# Testes
print(1, 1, 1, tipo_triangulo(1,1,1)) # Equilátero
print(1, 1, 2, tipo_triangulo(1,1,2)) # Isósceles
print(1, 2, 3, tipo_triangulo(1,2,3)) # Escaleno