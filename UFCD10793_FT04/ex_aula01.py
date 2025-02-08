'''
Exercício de aula 1: match ... case
Escreve um programa que receba o nome de um produto e o seu preço, e retorne o preço total considerando os descontos seguintes:

1. Se o produto for um smartphone, será aplicado um desconto de 10%.
2. Se o produto for um tablet, será aplicado um desconto de 15%.
3. Se o produto for um laptop, será aplicado um desconto de 20%.
4. Para qualquer outro produto, não haverá desconto.

Utilize a estrutura match ... case para determinar o desconto a ser aplicado.
'''


menu = '''
Escolha o pruduto / desconto a aplicar:
1. 10% para smartphone
2. 15% para tablet
3. 20% para laptop
4. qualquer outro sem desconto
'''


print(menu)
opcao = input('Insira a opção desejada: ')
preco_str = input('Insira o preço do produto: ')
preco = float(preco_str)

match opcao:
    case '1':
        desconto = 0.10
    case '2':
        desconto = 0.15
    case '3':
        desconto = 0.20
    case _:
        desconto = 0

print(f'O desconto é {desconto * 100:.0f}%')
preco_final = preco - preco * desconto
print(f'O preço final é {preco_final:.2f}')
