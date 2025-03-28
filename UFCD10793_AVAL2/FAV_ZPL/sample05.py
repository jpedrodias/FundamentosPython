'''
Sample 5 - FAV Enunciado ZPL
'''

import os, csv, tkinter as tk
from tkinter import filedialog, messagebox, ttk

import requests
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def gerar_etiquetas(csv_path, output_folder, tamanho_etiqueta):

    # Configuração da impressora e etiqueta
    dpi = '8dpmm'
    #size = '4x6'
    rotation = '0'
    labelary_url = f'https://api.labelary.com/v1/printers/{dpi}/labels/{tamanho_etiqueta}/{rotation}/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #source = 'data/produtos.csv' # escolhido pelo utilizador
    output_png = os.path.join(os.getcwd(), 'data', 'etiqueta_{}.png')
    output_pdf = os.path.join(os.getcwd(), 'data', 'etiquetas.pdf')
    #output_folder = os.path.join(os.getcwd(), 'data')

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

    c = canvas.Canvas(output_pdf, pagesize=A4)
    labels_per_page = 0

    x, y = x_margin, page_height - y_margin - label_height * 0.24

    for i, path in enumerate(etiquetas_paths):
        img = Image.open(path)
        img.thumbnail((label_width * 0.24, label_height * 0.24))
        img_path_temp = os.path.join(output_folder, f'_temp_{i}.png')
        img.save(img_path_temp, 'png')

        c.drawImage(img_path_temp, x, y)
        x += img.width + x_spacing
        if x + img.width > page_width - x_margin:
            x = x_margin
            y -= img.height + y_spacing
            if y < y_margin:
                c.showPage()
                x = x_margin
                y = page_height - y_margin - img.height
        labels_per_page += 1
    
    c.save()
    print(f'✓ PDF gerado com sucesso: {output_pdf}')
    messagebox.showinfo("Concluído", f"PDF gerado com sucesso: {output_pdf}")

    import glob
    for file in glob.glob(os.path.join(output_folder, '_temp_*.*')):
        os.remove(file)


# Função chamada ao clicar no cotão "Selecionar CSV"
def escolher_csv_onclick():
    caminho = filedialog.askopenfilename(
        title="Selecione o ficheiro CSV",
        filetypes=[("Ficheiros CSV", "*.csv")]
    )
    if caminho:
        csv_entry.delete(0, tk.END)
        csv_entry.insert(0, caminho)


def escolher_pasta_onclick():
    caminho = filedialog.askdirectory(title="Selecione a pasta de destino")
    if caminho:
        pasta_entry.delete(0, tk.END)
        pasta_entry.insert(0, caminho)


def iniciar_geracao():
    csv_path = csv_entry.get()
    output_folder = pasta_entry.get()
    tamanho_etiqueta = tamanho_combo.get()

    if not csv_path or not output_folder or not tamanho_etiqueta:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    gerar_etiquetas(csv_path, output_folder, tamanho_etiqueta)


# Interface gráfica (Tkinter) 
janela = tk.Tk()
janela.title("Gerador de Etiquetas")
janela.geometry("500x300")
janela.resizable(False, False)

# LAYOUT
frame = tk.Frame(janela, padx=20, pady=20)
frame.pack(fill='both', expand=True)


tk.Label(frame, text="Ficheiro CSV:").grid(row=0, column=0, sticky='w')
csv_entry = tk.Entry(frame, width=40)
csv_entry.grid(row=0, column=1, padx=5)

tk.Button(frame, text="Selecionar", command=escolher_csv_onclick).grid(row=0, column=2)

tk.Label(frame, text="Pasta de destino:").grid(row=1, column=0, sticky="w")
pasta_entry = tk. Entry(frame, width=40)
pasta_entry.grid(row=1, column=1, padx=5)
tk. Button(frame, text="Selecionar", command=escolher_pasta_onclick).grid(row=1, column=2)

tk. Label(frame, text="Tamanho da etiqueta:").grid(row=2, column=0, sticky="w")
tamanho_combo = ttk.Combobox(frame, values=["4x6", "2x1", "3x2", "4x2"], width=10)
tamanho_combo.grid(row=2, column=1, sticky="w")
tamanho_combo.set("4x6")

tk. Button(janela, text="Gerar Etiquetas", bg="#4CAF50", fg="white", height=2, command=iniciar_geracao).pack(pady=15)

janela.mainloop()

