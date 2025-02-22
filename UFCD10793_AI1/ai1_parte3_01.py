'''
Avaliação Intermédia 1 - Parte 3 - Exercício 1

1. Executar o ficheiro `banco_dados.py`
2. Verificar se foi criado um ficheiro chamado `empresa.sqlite`

Aplicações para consultar ficheiro .sqlite

(1) https://sqlitebrowser.org/
(2) https://dbeaver.io/
(3) Extensão no vscode: SQLite Viewer
(4) Só online: https://sqliteviewer.app/
'''

# 
import os
import banco_dados # as instruções de banco_dados.py são executadas

if os.path.exists('data/empresa.sqlite'):
    print('Ficheiro empresa.sqlite existe.')
else:
    print('Ficheiro empresa.sqlite não existe.')