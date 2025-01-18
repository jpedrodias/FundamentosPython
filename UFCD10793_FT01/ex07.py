'''
Faz um programa que receba a distância em km e a quantidade em litros de
combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve
uma mensagem de acordo com o resultado obtido. (deverá ser criado o ficheiro
ex07.py).

Exemplo: python ex07.py 100 10
'''

distancia = float(input('Introduza a distância percorrida em km: '))
litros = float(input('Introduza a quantidade de litros consumidos: '))
consumo = distancia / litros
print(f'O consumo foi de {consumo:.2f} km/l')
