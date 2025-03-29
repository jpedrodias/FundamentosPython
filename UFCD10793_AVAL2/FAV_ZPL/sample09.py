'''
Sample 9 - FAV Enunciado ZPL (page 22)
'''

import os, csv, tkinter as tk
from tkinter import filedialog, messagebox, ttk

import requests
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def gerar_etiquetas(csv_path, output_folder, tamanho_etiqueta):
    dpi = '8dpmm'
    rotation = '0'
    labelary_url = f'https://api.labelary.com/v1/printers/{dpi}/labels/{tamanho_etiqueta}/{rotation}/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    output_png = os.path.join(os.getcwd(), 'data', 'etiqueta_{}.png')
    output_pdf = os.path.join(os.getcwd(), 'data', 'etiquetas.pdf')

    fonte = fonte_entry.get()
    fonte_l = fonte_l_entry.get()
    fonte_h = fonte_h_entry.get()

    etiquetas_paths = []
    status_label.config(text="A preparar leitura do CSV...")
    janela.update_idletasks()
    with open(csv_path, newline='', mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        total = sum(1 for _ in reader)
        csvfile.seek(0)
        next(reader)

        for i, row in enumerate(reader):
            nome = row.get('nome')
            codigo = row.get('codigo')

            status_label.config(text=f'A gerar etiqueta {i + 1} de {total}...')
            janela.update_idletasks()

            # Criação do ZPL com texto, código de barras e QR Code
            zpl = f'''
^XA
^F050,50^{fonte}N, {fonte_h},{fonte_l}^FD{nome}^FS
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
                atualizar_preview(img_path)
                with open(img_path, 'wb') as f:
                    f.write(response.content)
                status_label.config(text=f'✓ Etiqueta {i + 1} de {total} gerada com sucesso.')
                janela.update_idletasks()
            else:
                messagebox.showerror("Erro", f"Erro ao gerar etiqueta {i + 1}: {nome}")
                return
    
    # Criação do PDF
    status_label.config(text="A criar PDF final...")
    janela.update_idletasks()

    criar_pdf(etiquetas_paths, output_folder, output_pdf)

    status_label.config(text=f'PDF concluído com Concluído')
    messagebox.showinfo("Concluído", f"PDF criado: {output_pdf}")
    

# Criar PDF com etiquetas
def criar_pdf(etiquetas_paths, output_folder, output_pdf):
    # === Criar PDF único com todas as etiquetas ===
    from PIL import Image
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4

    page_width, page_height = A4
    x_margin, y_margin = 30, 30
    x_spacing, y_spacing = 20, 20
    
    label_width, label_height = 800, 400

    c = canvas.Canvas(output_pdf, pagesize=A4)
    #labels_per_page = 0

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
        #labels_per_page += 1
    
    c.save()
    #print(f'✓ PDF gerado com sucesso: {output_pdf}')
    #messagebox.showinfo("Concluído", f"PDF gerado com sucesso: {output_pdf}")

    import glob
    for file in glob.glob(os.path.join(output_folder, '_temp_*.*')):
        os.remove(file)

# Atualiza o painel de imagem
def atualizar_preview(caminho_imagem):
    img = Image.open(caminho_imagem)
    img.thumbnail((250, 150))
    img_tk = ImageTk.PhotoImage(img)
    preview_label.config(image=img_tk)
    preview_label.image = img_tk 


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

    largura = largura_entry.get()
    altura = altura_entry.get()

    tamanho = f'{largura}x{altura}'

    if not csv_path or not output_folder or not tamanho:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    gerar_etiquetas(csv_path, output_folder, tamanho)


# Interface gráfica (Tkinter) 
janela = tk.Tk()
janela.title("Gerador de Etiquetas ZPL")
janela.geometry("700x500")
janela.resizable(False, False)


# LAYOUT
frame = tk.Frame(janela, padx=20, pady=10)
frame.pack(fill='x')


tk.Label(frame, text="Ficheiro CSV:").grid(row=0, column=0, sticky='w')
csv_entry = tk.Entry(frame, width=40)
csv_entry.grid(row=0, column=1, padx=5)

tk.Button(frame, text="Selecionar", command=escolher_csv_onclick).grid(row=0, column=2)

tk.Label(frame, text="Pasta de destino:").grid(row=1, column=0, sticky="w")
pasta_entry = tk. Entry(frame, width=40)
pasta_entry.grid(row=1, column=1, padx=5)
tk.Button(frame, text="Selecionar", command=escolher_pasta_onclick).grid(row=1, column=2)

tk.Label(frame, text="Tamanho da etiqueta (pol):").grid(row=2, column=0, sticky="w")
largura_entry = tk.Entry(frame, width=10)
largura_entry.grid(row=2, column=1, padx=5, sticky="w")
largura_entry.insert(0, "4")

tk.Label(frame, text="Altura (pol):").grid(row=2, column=0, sticky="e")
altura_entry = tk.Entry(frame, width=10)
altura_entry.grid(row=3, column=1, padx=5, sticky="w")
altura_entry.insert(0, "6") 


# Editor de texto para editar ZPL
tk.Label(frame, text="Fonte ZPL (ex: A0, A1):").grid(row=4, column=0, sticky="w")
fonte_entry = tk. Entry(frame, width=10)
fonte_entry.grid(row=4, column=1, sticky="w", padx=5)
fonte_entry.insert(0, "A0")

tk.Label(frame, text="Tamanho da fonte (larg x alt):").grid(row=5, column=0, sticky="w")
fonte_l_entry = tk. Entry(frame, width=5)
fonte_l_entry.grid(row=5, column=1, sticky="w", padx=(0,2))
fonte_l_entry.insert(0, "40")

fonte_h_entry = tk. Entry(frame, width=5)
fonte_h_entry.grid(row=5, column=1, sticky="e", padx=(2,0))
fonte_h_entry.insert(0, "40")



# Status
status_label = tk.Label(janela, text="Pronto", anchor="w")
status_label.pack(fill='x', padx=20, pady=5)

# Pré-visualização
preview_frame = tk.LabelFrame(janela, text="Pré-visualização da última etiqueta")
preview_frame.pack(padx=20, pady=10, fill='both', expand=True)
preview_label = tk.Label(preview_frame)
preview_label.pack(padx=10, pady=10)

# Botão final
tk. Button(janela, text="Gerar Etiquetas", bg="#4CAF50", fg="white", height=2, command=iniciar_geracao).pack(pady=15)


# Tema escuro
from dataclasses import dataclass
@dataclass(frozen=True)
class DarkTheme():
    DARK_BG = '#2E2E2E'
    DARK_ENTRY = '#3E3E3E'
    TEXT_COLOR = '#FFFFFF'
    ACCENT_COLOR = '#4CAF50'

janela.configure(bg=DarkTheme.DARK_BG)
frame.configure(bg=DarkTheme.DARK_BG)

for widget in frame.winfo_children():
    if isinstance(widget, tk.Label):
        widget.configure(bg=DarkTheme.DARK_BG, fg=DarkTheme.TEXT_COLOR)
    elif isinstance(widget, tk.Entry):
        #widget.configure(bg=DarkTheme.DARK_ENTRY, fg=DarkTheme.TEXT_COLOR, insertbackground=DarkTheme.TEXT_COLOR)
        # unknown option -bg ... -fg
        pass
    elif isinstance(widget, tk.Button):
        widget.configure(bg=DarkTheme.ACCENT_COLOR, fg="white", activebackground="#45A049")
    elif isinstance(widget, ttk.Combobox):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground=DarkTheme.DARK_ENTRY, background=DarkTheme.DARK_ENTRY, foreground=DarkTheme.TEXT_COLOR)

status_label.configure(bg=DarkTheme.DARK_BG, fg=DarkTheme.TEXT_COLOR)
preview_frame.configure(bg=DarkTheme.DARK_BG)
preview_label.configure(bg=DarkTheme.DARK_BG, fg=DarkTheme.TEXT_COLOR)

janela.mainloop()