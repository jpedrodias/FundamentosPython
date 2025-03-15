'''
Exercício 2 - funções com substituição da função interna print
'''

import builtins

class Cores:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'

def print(*args, **kwargs):
    cor = kwargs.get('cor', Cores.RESET)
    end = kwargs.get('end', '\n')
    texto = ' '.join(map(str, args))
    fancy = cor + texto + Cores.END 
    builtins.__dict__['__original_print__'](fancy, end=end)  # evita recursão infinita

# guardar referência original da função print
builtins.__original_print__ = builtins.print
builtins.print = print  # substituir print por fprint

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

# agora o 'print' já utiliza cores diretamente
print("Triangulo Equilátero", cor=Cores.BLUE)
print(1, 1, 1, tipo_triangulo(1,1,1))

print("Triangulo Isósceles", cor=Cores.RED)
print(1, 1, 2, tipo_triangulo(1,1,2))

print("Triangulo Escaleno", cor=Cores.GREEN)
print(1, 2, 3, tipo_triangulo(1,2,3), cor=Cores.RED)
