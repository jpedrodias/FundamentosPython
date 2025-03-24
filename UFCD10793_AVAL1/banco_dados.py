'''Sample code da ficha de avaliação UFCD10793_AI1'''

import sqlite3

# Criar conexão com o banco de dados (ou criar o ficheiro se não existir)

conn = sqlite3.connect('data/empresa.sqlite') # alterada a extensão para .sqlite
cursor = conn.cursor()

# Criar tabela de funcionários
SQL_CREATE_FUNCIONARIOS = '''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
);
'''

cursor.execute(SQL_CREATE_FUNCIONARIOS)

# Guardar as mudanças e fechar a conexão
conn.commit()
conn.close()
