'''
Exercício 1
Utilizando os ficheiros fornecidos, vamos reproduzir os exemplos da apresentação. Devem colocar os ficheiros .csv na pasta onde cria as scripts python.
Começam por abrir os ficheiros e analisar a informação nos mesmos
'''

# Alterar o diretório de trabalho para o diretório do script - necessário para quando executado no VSCode
from os import chdir, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)


# Instalar o módulo pandas
# pip install pandas

# import pandas
import pandas as pd

print(' * ler ficheiro cast.csv para dataframe casts')
casts = pd.read_csv('data/cast.csv', index_col=None)


# dados estatisticos do conjunto de dados
print(casts.describe())

# dados estatisticos do conjunto
print(casts.describe(include='all'))

# imprimir as cinco primeiras linhas do dataframe casts
print(casts.head())

# ler ficheiro titles.csv para dataframe titles
titles = pd.read_csv('data/titles.csv', index_col =None)


# imprimir as cinco últimas linhas do dataframe titles
print(titles.tail())

#alterar numero de linhas e colunas a visualizar sempre que se imprime todo o dataframe
pd.set_option('display.max_rows', 10, 'display.max_columns', 10)

# imprimir dataframe titles
print(titles)

# atribuir à variável tamanho o numero total d linhas do dataframe titles
tamanho=len(titles)

# imprimir tamanho
print(tamanho)

# imprimir primeiras três linhas do dataframe titles
print(titles.head(3))

# obter serie t a partir do dataframe titles selecionando a coluna title
t = titles['title'] 

# imprimir tipo de dados de t
print(type(t))

# Obter informação geral do dataframe casts
casts.info()

# imprimir linha de indice 0 no dataframe titles
print(titles.iloc[0])
