
'''
Exercício 4 - Bloco try/exception FileNotFoundError
Escreva um programa Python que abra um ficheiro e manipule uma exceção
FileNotFoundError se o arquivo não existir.
'''


def open_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:")
        print(contents)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")

# Usage
file_name = input("Input a file name: ")
open_file(file_name)

