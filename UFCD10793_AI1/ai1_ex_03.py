'''
Avaliação Intermédia 1 - Exercício 3

Verifique se um ficheiro existe antes de o abrir.
'''

# Exemplo 1
import os

try:
    caminho = input("Introduza o caminho do ficheiro: ")
    if os.path.exists(caminho):
        with open(caminho, 'r') as f:
            print(f.read())
    else:
        print("Erro: O ficheiro não foi encontrado.")
except FileNotFoundError:
    print("Erro: O ficheiro não foi encontrado.")
except Exception as e:
    print("Erro: inesperado", e)


# Exemplo 2 - using try only here is needed
import os
caminho = input("Introduza o caminho do ficheiro: ")
if os.path.exists(caminho):
    try:
        with open(caminho, 'r') as f:
            print(f.read())
    except Exception as e:
        print("Erro: inesperado", e)
else:
    print("Erro: O ficheiro não foi encontrado.")