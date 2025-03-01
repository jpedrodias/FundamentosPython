'''
Avaliação Intermédia 1 - Parte 3 - Exercício 3 - consultar dados

Depois de iniciada a conexão à base de dados, é executada a instrução SQL para consultar todos os funcionários da tabela `funcionarios`.

É chamado o método `fetchall()` para obter todos os resultados da consulta.

Por fim, é feito um loop para exibir os resultados.

'''

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

import sqlite3

print(__doc__)



conn = sqlite3.connect('data/empresa.sqlite')
cursor = conn.cursor()

# Consultar todos os funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor. fetchall()

# Exibir os resultados
for funcionario in funcionarios:
    #print(funcionario)
    id, nome, cargo, salario = funcionario
    print(f'ID: {id}, Nome: {nome}, Cargo: {cargo}, Salário: {salario}')

conn.close()

