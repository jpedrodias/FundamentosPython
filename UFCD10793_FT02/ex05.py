'''
Exercício 5 - função conversão unidades
Escreve um programa que faça a conversão para kms, de um dado valor em metros.
'''


# Obrigado à Infopédia por disponibilizar a informação sobre a palavra kilómetro
# https://www.infopedia.pt/dicionarios/lingua-portuguesa/kil%C3%B3metro
distancia_kms = input('Insere o valor em kilometros: ')

distancia_kms = float(distancia_kms)

distancia_metros = distancia_kms * 1000

print(f'A distância em metros é {distancia_metros}')
