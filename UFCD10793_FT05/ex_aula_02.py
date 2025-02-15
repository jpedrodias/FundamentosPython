'''
Exercício 2 - listas insert, append, remove, len, clear
Crie um programa para controlar listas, com as seguintes funções:
• Adicionar elemento no início;
• Adicionar elemento no fim;
• Remover elemento;
• Tamanho da lista;
• Imprimir elementos da lista;
• Esvaziar lista;
'''


# inicialização da lista
lista = []

# adicionar elemento no início
lista.insert(0, 'A')
lista.append(0, 'B')
lista.append(0, 'C')
print('Adicionados elementos inicio:', lista)

# adicionar elemento no fim
lista.append('D')
lista.append('E')
lista.append('F')
print('Adicionados elementos fim:', lista)

# remover elemento
lista.remove('A')
print('Removido um elemento:', lista)

# tamanho da lista
print('O tamanho da lista é:', len(lista))

# Esvaziar lista
lista.clear()