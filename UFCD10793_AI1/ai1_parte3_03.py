'''
Avaliação Intermédia 1 - Parte 3 - Exercício 3 - consultar dadis

Depois de iniciada a conexão à base de dados, é executada a instrução SQL para consultar todos os funcionários da tabela `funcionarios`.

É chamado o método `fetchall()` para obter todos os resultados da consulta.

Por fim, é feito um loop para exibir os resultados.

'''

print(__doc__)

import sqlite3

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

