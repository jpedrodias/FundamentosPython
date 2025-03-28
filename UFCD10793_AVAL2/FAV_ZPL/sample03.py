'''
Sample 3 - FAV Enunciado ZPL
'''
import os, csv, requests

# change the working directory to the script's directory
workdir = os.path.dirname(os.path.abspath(__file__))
os.chdir(workdir)

# Configuração da impressora e etiqueta
from dataclasses import dataclass

@dataclass
class Config:
    dpi = '8dpmm'
    size = '4x6'
    rotation = '0'
    labelary_url = f'https://api.labelary.com/v1/printers/{dpi}/labels/{size}/{rotation}/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    source = 'data/produtos.csv'
    output_png = 'data/etiqueta_{}.png'
    output_folder = 'data/'
    output_pdf = 'data/etiqueta_todas.pdf'

# Define a pasta de saída
os.makedirs(Config.output_folder, exist_ok=True)


# Lê os dados do CSV e gera etiquetas
etiquetas_paths = []
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
            output_filename = Config.output_png.format(i+1)
            etiquetas_paths.append(os.path.join(workdir, output_filename))

            with open(output_filename, 'wb') as f:
                f.write(response.content)
            print(f'✓ Etiqueta {i+1} gerada com sucesso: {nome}')

        else:
            print(f'✗ Erro ao gerar etiqueta {i+1}: {response.status_code} - {response.text}')

        
        

# === Criar PDF único com todas as etiquetas ===
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

@dataclass
class PdfConfig:
    page_width, page_height = A4
    x_margin, y_margin = 30, 30
    x_spacing, y_spacing = 20, 20
    
    label_width, label_height = 800, 400
    


c = canvas.Canvas(Config.output_pdf, pagesize=A4)
labels_per_page = 0
x, y = PdfConfig.x_margin, PdfConfig.page_height - PdfConfig.y_margin - PdfConfig.label_height * 0.24
for i, path in enumerate(etiquetas_paths):
    img = Image.open(path)
    img.thumbnail((PdfConfig.label_width * 0.24, PdfConfig.label_height * 0.24))
    img_path_temp = os.path.join(Config.output_folder, f'_temp_{i}.png')
    img.save(img_path_temp, 'JPEG')

    c.drawImage(img_path_temp, x, y)

    x += img.width + PdfConfig.x_spacing
    if x + img.width > PdfConfig.page_width - PdfConfig.x_margin:
        x = PdfConfig.x_margin
        y -= img.height + PdfConfig.y_spacing
        if y < PdfConfig.y_margin:
            c.showPage()
            x = PdfConfig.x_margin
            y = PdfConfig.page_height - PdfConfig.y_margin - img.height
        
    labels_per_page += 1
c.save()
print(f'✓ PDF gerado com sucesso: {Config.output_pdf}')


# Remove temporary images im blob (_temp_*.png)
print('Cleaning temp files...')
import glob
for file in glob.glob(os.path.join(Config.output_folder, '_temp_*.*')):
    os.remove(file)

