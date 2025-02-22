'''
Avaliação Intermédia 1 - Parte 3 - Exercício 6 - CRUD System com SQLite
'''

import sqlite3, os

print(__doc__)

DATABASE = 'data/empresa.sqlite'

def draw_box(title, items, WIDTH=80):
    width = WIDTH - 2
    print('╔' + '═' * width + '╗')
    size = width - 1 - len(title)
    print(f'║ {title}{" " * size}║█')

    print('╠' + '═' * width + '╣█')
    for item in items:
        size = width - 1 - len(item)
        print(f'║ {item}{" " * size}║█')
    print('╚' + '═' * width + '╝█')
    print(' ' + '▀' * (width + 2))


def find_menu_key(menu_items, key):
    index = -1
    keys = [i for i, item in enumerate(menu_items) if item['key'] == key] # Procurar o índice/key do item no menu
    if len(keys) == 1:
        index = keys[0]
    return index
    

def main():    
    global cursor

    MENU_ITEMS = [

        {'key': '1', 'description': 'Adicionar funcionário',
         'SQL': 'INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)',
         'HEAD': 'CREAT| Nome                                     | Cargo          | Salário'},

        {'key': '2', 'description': 'Listar funcionários',
         'SQL': 'SELECT * FROM funcionarios',
         'HEAD': ' ID  | Nome                                     | Cargo          | Salário'},

        {'key': '3', 'description': 'Atualizar salário',
         'SQL': 'UPDATE funcionarios SET salario = ? WHERE nome = ?',
         'HEAD': 'UPDAT| Nome                                     | Cargo          | Salário'},

        {'key': '4', 'description': 'Eliminar funcionário',
         'SQL': 'DELETE FROM funcionarios WHERE nome = ?',
         'HEAD': 'DELET| Nome                                     | Cargo          | Salário'},
    
        {'key': '5', 'description': 'Sair', 'SQL': ''},

        {'key': '0', 'description': 'Criar tabela/base de dados',
         'SQL': '''CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
    )''' },

    ]
    
    if os.path.exists(DATABASE):
        print(f'Ficheiro {DATABASE} já existe.')
    else:
        print(f'Ficheiro {DATABASE} ainda não existe.') 
    
    end_program = False
    while end_program == False:
        
        menu_items = [f'{item["key"]}. {item["description"]}' for item in MENU_ITEMS]
        draw_box('MENU PRINCIPAL - CRUD (Create, Read, Update and Delete)', menu_items)

        key = input(' » Escolha uma opção: ')
        match key:
            case '0':
                print('Criar tabela/base de dados')

                menu_index = find_menu_key(MENU_ITEMS, key)
                sql_cmd = MENU_ITEMS[menu_index].get('SQL')

                cursor.execute(sql_cmd)
                conn.commit()
                print('Tabela criada com sucesso.')
                continuar = input('Prima ENTER para continuar...')

            case '1':
                print('Adicionar funcionário')

                menu_index = find_menu_key(MENU_ITEMS, key)
                sql_cmd = MENU_ITEMS[menu_index].get('SQL')
                
                nome = input('Nome: ')
                cargo = input('Cargo: ')
                salario = float(input('Salário: '))

                menu_items = []
                menu_head = MENU_ITEMS[menu_index].get('HEAD')
                texto_id = f' NEW'
                texto_nome = f'{nome:<40}'
                texto_cargo = f'{cargo:<14}'
                texto_salario = f'{salario:10.2f}'
                texto = f'{texto_id} | {texto_nome} | {texto_cargo} | {texto_salario}'
                menu_items.append(texto)
                draw_box(menu_head, menu_items)
                confirmacao = input('Pretende adicionar este funcionário (S/N): ')
                if confirmacao.upper() == 'S':
                    cursor.execute(sql_cmd, (nome, cargo, salario))
                    conn.commit()
                    print('Funcionário adicionado com sucesso.')
                else:
                    print('Operação cancelada.')
                continuar = input('Prima ENTER para continuar...')

            case '2':
                print('Listar funcionários')

                menu_index = find_menu_key(MENU_ITEMS, key)
                sql_cmd = MENU_ITEMS[menu_index].get('SQL')

                cursor.execute(sql_cmd)
                funcionarios = cursor.fetchall()

                menu_items = []
                menu_head = MENU_ITEMS[menu_index].get('HEAD')
                for funcionario in funcionarios:
                    id, nome, cargo, salario = funcionario
                    texto_id = f'{id:4d}'
                    texto_nome = f'{nome:<40}'
                    texto_cargo = f'{cargo:<14}'
                    texto_salario = f'{salario:10.2f}'
                    texto = f'{texto_id} | {texto_nome} | {texto_cargo} | {texto_salario}'
                    menu_items.append(texto)
                print(f'LISTA DE FUNCIONÁRIOS: {len(menu_items)}')
                draw_box(menu_head, menu_items)
                continuar = input('Prima ENTER para continuar...')

            case '3':
                print('Atualizar salário')

                menu_index = find_menu_key(MENU_ITEMS, key)
                sql_cmd = MENU_ITEMS[menu_index].get('SQL')

                nome = input('Nome do funcionário: ')
                novo_salario = float(input('Salário: '))
                confirmacao = input('Pretende alterar o salário a este funcionário (S/N): ')
                if confirmacao.upper() == 'S':
                    cursor.execute(sql_cmd, (novo_salario, nome))
                    conn.commit()
                else:
                    print('Operação cancelada.')
                continuar = input('Prima ENTER para continuar...')
                
            case '4':
                print('Eliminar funcionário')

                menu_index = find_menu_key(MENU_ITEMS, key)
                sql_cmd = MENU_ITEMS[menu_index].get('SQL')

                nome = input('Nome do funcionário a eliminar: ')
                confirmacao = input('Pretende eliminar este funcionário (S/N): ')
                if confirmacao.upper() == 'S':
                    cursor.execute(sql_cmd, (nome,))
                    conn.commit()
                else:
                    print('Operação cancelada.')

            case '5':
                print('Aplicação terminada. Tenha um bom dia!')
                end_program = True
            case _:
                print('Opção inválida.')
    conn.close()

if __name__ == '__main__':
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    main()