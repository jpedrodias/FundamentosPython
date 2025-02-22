'''
Avaliação Intermédia 1 - Parte 3 - Exercício 6 - Eliminar dados
'''

print(__doc__)

import sqlite3, time

conn = sqlite3.connect('data/empresa.sqlite')
cursor = conn.cursor()

# 1. Eliminar o funcionário
print('A eliminar funcionário Mariana Costa...')
SQL_DELETE_FUNCIONARIO = "DELETE FROM funcionarios WHERE nome = 'Mariana Costa'"
cursor.execute(SQL_DELETE_FUNCIONARIO)
conn.commit()

print('A eliminar funcionário com salário inferior a 3000.00...')
SQL_DELETE_FUNCIONARIOS = "DELETE FROM funcionarios WHERE salario < 3000.00"
cursor.execute(SQL_DELETE_FUNCIONARIOS)
conn.commit()


conn.close()