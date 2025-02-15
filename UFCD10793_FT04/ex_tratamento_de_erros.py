'''
Alternativas para deteção/tratamento de dados inválidos
'''


# detetar se o utilizador introduziu um número inteiro
n = ''
while not n.lstrip('-').isdigit():
    n = input('Numero: ')


# alternaativa usando try except
n = None
while n is None:
    try:
        n = int(input('Numero: '))
    except:
        n = None

# alternativa usando regular expressions
import re

n = ''
while not bool(re.fullmatch(r"-?\d+", n)):
    n = input('Numero: ')
    


n = int(n)
soma = 0
for i in range(1, n+1):
    soma += i 
print(soma)