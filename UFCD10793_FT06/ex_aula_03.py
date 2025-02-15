'''
Exercício 3 - listas
Considera a lista
 idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]

 Cria um programa, em python, que:
    a. Indique quantas pessoas são menores de idade
    b. Ordene a lista por ordem decrescente
    c. Pede ao utilizador uma idade e verifica se essa idade está na lista.
        #- Se estiver faz print("A idade está na lista")
        #- Caso contrário faz o print("não existe ninguém com essa idade na lista")
'''

idades = [25, 15, 19, 22, 37, 78, 46, 2, 67]

# a. Indique quantas pessoas são menores de idade

# método 1
menores = 0
for idade in idades:
    if idade < 18:
        menores += 1

print(f'(*1) Existem {menores} pessoas menores de idade')

# método 2
menores = len([idade for idade in idades if idade < 18])
print(f'(*2) Existem {menores} pessoas menores de idade')

# método 3:
menores = sum(1 for idade in idades if idade < 18)
print(f'(*3) Existem {menores} pessoas menores de idade')


# b. Ordene a lista por ordem decrescente
idades.sort(reverse=True)
print('Idades ordenadas por ordem decrescente:', idades)

# c. Pede ao utilizador uma idade e verifica se essa idade está na lista.
#     #- Se estiver faz print("A idade está na lista")
#     #- Caso contrário faz o print("não existe ninguém com essa idade na lista")

idade = int(input('Indique uma idade: '))
if idade in idades:
    print('A idade está na lista')
else:
    print('Não existe ninguém com essa idade na lista')
    
