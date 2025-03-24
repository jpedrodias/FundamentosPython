'''
Avaliação Intermédia 1 - Parte 1 - Exercício 3 (b)

Verifique se um ficheiro existe antes de o abrir.
'''

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

