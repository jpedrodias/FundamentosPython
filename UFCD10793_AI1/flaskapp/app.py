from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3
import os

DATABASE = '../data/empresa.sqlite'

def get_db_connection():
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    return conn, conn.cursor()


# Criação da base de dados e tabela
conn, cursor = get_db_connection()
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
)
''')
conn.commit()
conn.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret key - this is the salt used to encrypt the session'


@app.route('/')
def index():
    conn, cursor = get_db_connection()
    funcionarios = cursor.execute('SELECT * FROM funcionarios').fetchall()

    funcionarios_lista = []
    for funcionario in funcionarios:
        id, nome, cargo, salario = funcionario
        funcionarios_lista.append({'id': id, 'nome': nome, 'cargo': cargo, 'salario': salario})

    conn.close()
    return render_template('index.html', funcionarios=funcionarios_lista)


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cargo = request.form.get('cargo')
        salario = request.form.get('salario')

        if '' in [nome, cargo, salario]:
            flash('Os campos não podem estar vazios!', 'warning')
            return redirect(url_for('index'))
        
        try:
            salario = float(salario)
        except ValueError:
            flash('O salário tem de ser um número!', 'warning')
            return redirect(url_for('index'))
        
        if salario < 0:
            flash('O salário tem de ser um número positivo!', 'warning')
            return redirect(url_for('index'))
        

        conn, cursor = get_db_connection()
        cursor.execute('INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)', (nome, cargo, salario))
        conn.commit()
        conn.close()
        flash('Funcionário adicionado com sucesso!', 'success')
        return redirect(url_for('index'))

    return 'Este URL só aceita pedidos POST!'

@app.route('/update/<int:id>', methods=['POST'])
def update(id=None):
    if request.method == 'POST':
        nome = request.form.get('nome')
        cargo = request.form.get('cargo')
        salario = request.form.get('salario')

        if '' in [nome, cargo, salario]:
            flash('Os campos não podem estar vazios!', 'warning')
            return redirect(url_for('index'))
        
        try:
            salario = float(salario)
        except ValueError:
            flash('O salário tem de ser um número!', 'warning')
            return redirect(url_for('index'))
        
        if salario < 0:
            flash('O salário tem de ser um número positivo!', 'warning')
            return redirect(url_for('index'))
        
        conn, cursor = get_db_connection()
        cursor.execute('SELECT * FROM funcionarios WHERE id = ?', (id,))
        funcionario = cursor.fetchone()
        if funcionario is None:
            flash('Funcionário não encontrado!', 'warning')
            return redirect(url_for('index'))
        
        cursor.execute('UPDATE funcionarios SET nome = ?, cargo = ?, salario = ? WHERE id = ?', (nome, cargo, salario, id))
        conn.commit()
        conn.close()
        flash('Funcionário atualizado com sucesso!', 'success')
        return redirect(url_for('index'))

    return 'Este URL só aceita pedidos POST!'

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id=None):
    if request.method == 'POST':
        conn, cursor = get_db_connection()
        cursor.execute('SELECT * FROM funcionarios WHERE id = ?', (id,))
        funcionario = cursor.fetchone()
        if funcionario is None:
            flash('Funcionário não encontrado!', 'warning')
            return redirect(url_for('index'))
        
        id, nome, cargo, salario = funcionario

        cursor.execute('DELETE FROM funcionarios WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash(f'Funcionário {nome} eliminado com sucesso!', 'danger')
        return redirect(url_for('index'))

    return 'Este URL só aceita pedidos POST!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    