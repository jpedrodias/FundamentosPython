'''
Avaliação Intermédia 1 - Parte 3 - Exercício 2
'''

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)


import sqlite3

conn = sqlite3.connect('data/empresa.sqlite')
cursor = conn.cursor()

# Inserir funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 2000)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 1500)")


# 1. Acrecenta mais dois funcionários à dase de daods, alterando o código acime
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('João Silva', 'Gestor', 3000)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Rita Santos', 'Programador', 2500)")

# Guardar mudanças e fechar conexão
conn.commit()
conn.close()