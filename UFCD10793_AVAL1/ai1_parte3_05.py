'''
Avaliação Intermédia 1 - Parte 3 - Exercício 6 - Eliminar dados
'''

import sqlite3, time

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

print(__doc__)



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