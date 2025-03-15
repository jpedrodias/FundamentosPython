'''
Exercício Aula 1 - Strings strip, slice e upper
1. Escreva um programa que, dada uma sequência de números inteiros (todos fornecidos na mesma linha, separados por espaços), imprima a média desses números.

2. Escreva um programa que, dada uma String representando um texto, imprima o número de palavras existentes.
Observação: você deve remover os sinais de pontuação (".", ", ", ":", "; ", "!" e"?") antes de realizar a contagem das palavras.
'''

# Exercício 1
numeros = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
numeros = [int(value) for value in numeros.split(',')]

print('Média desses números é', sum(numeros)/len(numeros))


# Exercício 2
char_to_remove = ['.', ',', ':', ';', '!', '?', '\n', '\"', '=']
texto = '''

Exemplo de texto. Este é um exemplo de texto, com sinais de pontuação: ponto e vírgula; exclamação! interrogação?
Se uma palavra aparecer mais do que uma vez, deve ser contada apenas uma vez.
Por exemplo, "sim, sim, pois pois pois", é igual a sim = 2 e pois = 3.
'''

for char in char_to_remove:
    texto = texto.replace(char, ' ')

palavras = texto.lower().split(' ') # usar lower() para ignorar case insensitive
print('Número de palavras com repetições:', len(palavras))


# Usando set para remover repetições
print('Número de palavras sem repetições:', len(set(palavras)))

# Usando dicionário para contar palavras
dicionario = {}
for palavra in palavras:
    palavra = palavra.lower() 
    dicionario[palavra] = dicionario.get(palavra, 0) + 1
print('Número de palavras com repetições:', len(dicionario))
print('Palavras únicas:', dicionario)


