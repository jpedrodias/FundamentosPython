'''
Sample 2 - FAV Enunciado ZPL
'''
import os, csv, requests

# change the working directory to the script's directory
workdir = os.path.dirname(os.path.abspath(__file__))
os.chdir(workdir)


# Define a pasta de saída
os.makedirs('data', exist_ok=True)

# Configuração da impressora e etiqueta
from dataclasses import dataclass

@dataclass
class Config:
    dpi = '8dpmm'
    size = '4x6'
    rotation = '0'
    labelary_url = f'https://api.labelary.com/v1/printers/{dpi}/labels/{size}/{rotation}/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    source = 'data/sample02.csv'
    output = 'data/etiqueta_{}.png'


# Lê os dados do CSV e gera etiquetas
with open(Config.source, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        nome = row.get('nome')
        codigo = row.get('codigo')

        # Criação do ZPL para cada produto
        zpl = f'''
^XA
^FO50,50^A0N,40,40^FD{nome}^FS
^FO50,120^BCN,100,Y,N,N
^FD{codigo}^FS
^XZ
'''

        # Envio do ZPL para a impressora
        response = requests.post(Config.labelary_url, headers=Config.headers, data=zpl.strip().encode('utf-8'))

        if response.status_code == 200:
            output_filename = Config.output.format(i+1)
            with open(output_filename, 'wb') as f:
                f.write(response.content)
            print(f'Etiqueta {i+1} gerada com sucesso: {nome}')
        else:
            print(f'Erro ao gerar etiqueta {i+1}: {response.status_code} - {response.text}')

        
        

