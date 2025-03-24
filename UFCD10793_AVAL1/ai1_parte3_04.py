'''
Avaliação Intermédia 1 - Parte 3 - Exercício 4 - atualizar dados
'''

import sqlite3, time

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

print(__doc__)



conn = sqlite3.connect('data/empresa.sqlite')
cursor = conn.cursor()

# 1. Atualizar o salário de Pedro Santos
SQL_UPDATE_SALARIO = "UPDATE funcionarios SET salario = 3000.00 WHERE nome = 'Pedro Santos'"
cursor.execute(SQL_UPDATE_SALARIO)

# 2. Aumentar o salário de todos os funcionários em 5%
#SQL_UPDATE_SALARIO = "UPDATE funcionarios SET salario = salario * 1.05"
#cursor.execute(SQL_UPDATE_SALARIO)

cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor. fetchall()
for funcionario in funcionarios:
    id, nome, cargo, salario = funcionario
    novo_salario = salario * 1.05
    print(f'ID: {id}, Nome: {nome}, Cargo: {cargo}, Salário: {salario} -> {novo_salario}')
    SQL_UPDATE_SALARIO = f"UPDATE funcionarios SET salario = {novo_salario} WHERE id = {id}"
    cursor.execute(SQL_UPDATE_SALARIO)
    conn.commit()    
    time.sleep(1)

conn.commit()
conn.close()
