'''
Exercício 2 - match - estado civil
Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de uma pessoa.
'''

estado_civil = input('Insira o estado civil (S, C ou V): ')
estado_civil = estado_civil.upper()

match estado_civil:
    case 'S':
        estado_civil_str = 'Solteiro'
    case 'C':
        estado_civil_str = 'Casado'
    case 'V':
        estado_civil_str = 'Viúvo'
    case _: # default
        estado_civil_str = 'Estado civil inválido'

print('Estado civil:', estado_civil_str)
