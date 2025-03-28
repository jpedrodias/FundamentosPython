'''
Sample 4 - FAV Enunciado ZPL
'''

import os, csv, tkinter as tk
from tkinter import filedialog, messagebox

import requests
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def gerar_etiquetas(csv_path):

    # Configuração da impressora e etiqueta
    dpi = '8dpmm'
    size = '4x6'
    rotation = '0'
    labelary_url = f'https://api.labelary.com/v1/printers/{dpi}/labels/{size}/{rotation}/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    source = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
    output_png = os.path.join(os.getcwd(), 'data', 'etiqueta_{}.png')
    output_pdf = os.path.join(os.getcwd(), 'data', 'etiquetas.pdf')
    output_folder = os.path.join(os.getcwd(), 'data')

    # Lê os dados do CSV e gera etiquetas
    etiquetas_paths = []
    with open(csv_path, newline='', mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            nome = row.get('nome')
            codigo = row.get('codigo')

            # Criação do ZPL com texto, código de barras e QR Code
            zpl = f'''
^XA
^F050, 50^AON, 40,40^FD{nome}^FS
^F050,120^BCN,100,Y,N,N
^FD{codigo}^FS
^F050,250^BQN,2,5
^FDLA, {codigo}^FS
^XZ
'''
            response = requests.post(labelary_url, headers=headers, data=zpl.strip().encode('utf-8'))
            if response.status_code == 200:
                img_path = os.path.join(output_folder, output_png.format(i + 1))
                etiquetas_paths.append(img_path)
                with open(img_path, 'wb') as f:
                    f.write(response.content)
                print(f'✓ Etiqueta {i + 1} gerada com sucesso: {nome}')
            else:
                print(f'✗ Erro ao gerar etiqueta {i + 1}: {response.status_code} - {response.text}')
                messagebox.showerror("Erro", f"Erro ao gerar etiqueta {i + 1}: {nome}")
            
    
    # === Criar PDF único com todas as etiquetas ===
    from PIL import Image
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    page_width, page_height = A4
    x_margin, y_margin = 30, 30
    x_spacing, y_spacing = 20, 20
    
    label_width, label_height = 800, 400

    