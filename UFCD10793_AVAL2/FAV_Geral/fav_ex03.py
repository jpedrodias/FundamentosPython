'''
Exercício 3 - FAV Enunciado Geral

Escreve  uma  função  em  Python  que  dada  uma  lista  de  números  imprime  a  soma  dos 
valores  dessa  lista,  o  número  de  elementos da  lista e  a  media  desses  valores.  
Implementa tratamento de exceções no teu código (try...except...else..finally).
'''

def fibonacci(n):
    '''Retorna o n-ésimo número da sequência de Fibonacci'''
    if n < 0:
        raise ValueError('O número deve ser positivo')
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def sequencia_fibonacci(n):
    '''Retorna os n primeiros números da sequência de Fibonacci'''
    return [fibonacci(i) for i in range(2, n+2)]


'''
Tratamentos de exceções
'''
# Criação de um tipo erro personalizado
class ListaVaziaError(Exception):
    '''Exceção personalizada para listas vazias.'''
    pass

def tratamento_dos_numeros(numeros):
    try:
        if not numeros:
            raise ListaVaziaError('A lista está vazia')
        
        for n in numeros:
            if not isinstance(n, (int, float)):
                raise TypeError('A lista deve conter apenas números inteiros ou reais')    

            if n < 0:
                raise ValueError('A lista deve conter apenas números positivos')
            
        soma = sum(numeros)
        media = soma / len(numeros)

    except ListaVaziaError as e:
        print(f'Erro: {e}')

    except TypeError as e:
        print(f'Erro: a lista deve conter apenas números inteiros ou reais')

    except ValueError as e:
        print(f'Erro: a lista deve conter apenas números positivos')

    except Exception as e:
        print(f'Erro: {e}')

    else:
        print(f'Soma dos valores: {soma}')
        print(f'Número de elementos: {len(numeros)}')
        print(f'Média dos valores: {media}')

    finally:
        print('Análise concluída')

'''
Situações de testes que vão gerar os vários tipos de erros
'''


size = 10
numeros = sequencia_fibonacci(size)
print('Sequencia de Fibonacci:', numeros)
print(numeros)


print('\nLista Vazia irá gerar erro de lista vazia')
tratamento_dos_numeros([])

print('\nLista com textos, irá gerar erro de tipo')
tratamento_dos_numeros(numeros + ['a'])

print('\nLista com valores negativos, irá gerar erro de valor')
tratamento_dos_numeros(numeros + ['-1'])

print('\nLista sem valores negativos e sem textos')
tratamento_dos_numeros(numeros)