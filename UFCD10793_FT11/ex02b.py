'''
Exercício 2 - funções com substituição da função interna print
'''

from my_fancy_terminal import print, Colors as Cores

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

# agora o 'print' já utiliza cores diretamente
print("Triangulo Equilátero", color=Cores.BLUE)
print(1, 1, 1, tipo_triangulo(1,1,1))

print("Triangulo Isósceles", color=Cores.RED)
print(1, 1, 2, tipo_triangulo(1,1,2))

print("Triangulo Escaleno", color=Cores.GREEN)
print(1, 2, 3, tipo_triangulo(1,2,3), color=Cores.RED)
