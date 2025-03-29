'''
Gerador de etiquetas ZPL com pré-visualização e envio para impressora Zebra
'''

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import csv
import requests
import socket
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# === Função para atualizar imagem de pré-visualização ===
def atualizar_preview(caminho_imagem):
    try:
        img = Image.open(caminho_imagem)
        img.thumbnail((250, 150))
        img_tk = ImageTk.PhotoImage(img)
        preview_label.config(image=img_tk)
        preview_label.image = img_tk
    except:
        pass

# === Função principal ===
def gerar_etiquetas(csv_path, output_folder, largura, altura, fonte, fonte_l, fonte_h):
    dpi = "8dpmm"
    rotation = "0"
    tamanho_etiqueta = f"{largura}x{altura}"
    labelary_url = f"https://api.labelary.com/v1/printers/{dpi}/labels/{tamanho_etiqueta}/{rotation}/"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    pdf_final = os.path.join(output_folder, "etiquetas_todas.pdf")
    os.makedirs(output_folder, exist_ok=True)
    etiqueta_paths = []

    try:
        status_label.config(text="A preparar leitura do CSV...")
        janela.update_idletasks()

        with open(csv_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            total = sum(1 for _ in reader)
            csvfile.seek(0)
            next(reader)

            for i, row in enumerate(reader):
                nome = row["nome"]
                codigo = row["codigo"]

                status_label.config(text=f"A gerar etiqueta {i+1} de {total}...")
                janela.update_idletasks()

                zpl = f"""
                ^XA
                ^FO50,50^{fonte}N,{fonte_h},{fonte_l}^FD{nome}^FS
                ^FO50,120^BCN,100,Y,N,N
                ^FD{codigo}^FS
                ^FO50,250^BQN,2,5
                ^FDLA,{codigo}^FS
                ^XZ
                """

                if enviar_check.get() == 1:
                    try:
                        ip = ip_entry.get()
                        porta = int(porta_entry.get())

                        status_label.config(text=f"A enviar etiqueta {i+1} para {ip}:{porta}...")
                        janela.update_idletasks()

                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as zebra_socket:
                            zebra_socket.connect((ip, porta))
                            zebra_socket.sendall(zpl.encode('utf-8'))

                        status_label.config(text=f"Etiqueta {i+1} enviada com sucesso.")
                    except Exception as e:
                        messagebox.showerror("Erro de envio", f"Falha ao enviar etiqueta: {e}")
                        return
                else:
                    response = requests.post(labelary_url, data=zpl.strip(), headers=headers)

                    if response.status_code == 200:
                        img_path = os.path.join(output_folder, f"etiqueta_{i+1}.png")
                        with open(img_path, "wb") as f:
                            f.write(response.content)
                        etiqueta_paths.append(img_path)
                        atualizar_preview(img_path)
                    else:
                        messagebox.showerror("Erro", f"Erro ao gerar etiqueta {i+1}: {response.status_code}")
                        return

        status_label.config(text="A criar PDF final...")
        janela.update_idletasks()
        criar_pdf(etiqueta_paths, output_folder, pdf_final)

        status_label.config(text="PDF concluído com sucesso!")
        messagebox.showinfo("Concluído", f"PDF criado: {pdf_final}")

    except Exception as e:
        status_label.config(text="Erro durante o processo.")
        messagebox.showerror("Erro", str(e))

# === Cria o PDF ===
def criar_pdf(etiqueta_paths, output_folder, pdf_final):
    c = canvas.Canvas(pdf_final, pagesize=A4)
    page_width, page_height = A4
    x_margin, y_margin = 30, 30
    x_spacing, y_spacing = 20, 20
    label_width, label_height = 800, 480

    x = x_margin
    y = page_height - y_margin - label_height * 0.24

    for i, path in enumerate(etiqueta_paths):
        img = Image.open(path)
        img.thumbnail((label_width * 0.24, label_height * 0.24))
        temp_jpg = os.path.join(output_folder, f"_tmp_{i}.jpg")
        img.save(temp_jpg, "JPEG")
        c.drawImage(temp_jpg, x, y)

        x += img.width + x_spacing
        if x + img.width > page_width - x_margin:
            x = x_margin
            y -= img.height + y_spacing
            if y < y_margin:
                c.showPage()
                x = x_margin
                y = page_height - y_margin - img.height

    c.save()

# === Interface ===
def escolher_csv():
    caminho = filedialog.askopenfilename(title="Selecionar CSV", filetypes=[("CSV", "*.csv")])
    if caminho:
        csv_entry.delete(0, tk.END)
        csv_entry.insert(0, caminho)

def escolher_pasta():
    caminho = filedialog.askdirectory(title="Selecionar pasta")
    if caminho:
        pasta_entry.delete(0, tk.END)
        pasta_entry.insert(0, caminho)

def iniciar_geracao():
    csv_path = csv_entry.get()
    output_folder = pasta_entry.get()
    largura = largura_entry.get()
    altura = altura_entry.get()
    fonte = fonte_entry.get()
    fonte_l = fonte_l_entry.get()
    fonte_h = fonte_h_entry.get()

    if not csv_path or not output_folder:
        messagebox.showwarning("Atenção", "Seleciona o CSV e a pasta de destino.")
        return

    gerar_etiquetas(csv_path, output_folder, largura, altura, fonte, fonte_l, fonte_h)

# === GUI ===
janela = tk.Tk()
janela.title("Gerador de Etiquetas ZPL")
janela.geometry("750x500")
janela.configure(bg="#2E2E2E")

frame = tk.Frame(janela, padx=20, pady=10, bg="#2E2E2E")
frame.pack(fill="x")

# Campos CSV e pasta
tk.Label(frame, text="Ficheiro CSV:", bg="#2E2E2E", fg="white").grid(row=0, column=0, sticky="w")
csv_entry = tk.Entry(frame, width=40, bg="#3C3C3C", fg="white", insertbackground="white")
csv_entry.grid(row=0, column=1, padx=5)
tk.Button(frame, text="Selecionar", command=escolher_csv, bg="#4CAF50", fg="white").grid(row=0, column=2)

tk.Label(frame, text="Pasta de destino:", bg="#2E2E2E", fg="white").grid(row=1, column=0, sticky="w")
pasta_entry = tk.Entry(frame, width=40, bg="#3C3C3C", fg="white", insertbackground="white")
pasta_entry.grid(row=1, column=1, padx=5)
tk.Button(frame, text="Selecionar", command=escolher_pasta, bg="#4CAF50", fg="white").grid(row=1, column=2)

# Tamanho

tk.Label(frame, text="Largura (pol):", bg="#2E2E2E", fg="white").grid(row=2, column=0, sticky="w")
largura_entry = tk.Entry(frame, width=10, bg="#3C3C3C", fg="white")
largura_entry.grid(row=2, column=1, sticky="w", padx=5)
largura_entry.insert(0, "4")

tk.Label(frame, text="Altura (pol):", bg="#2E2E2E", fg="white").grid(row=3, column=0, sticky="w")
altura_entry = tk.Entry(frame, width=10, bg="#3C3C3C", fg="white")
altura_entry.grid(row=3, column=1, sticky="w", padx=5)
altura_entry.insert(0, "6")

# Fonte ZPL
tk.Label(frame, text="Fonte ZPL (ex: A0):", bg="#2E2E2E", fg="white").grid(row=4, column=0, sticky="w")
fonte_entry = tk.Entry(frame, width=10, bg="#3C3C3C", fg="white")
fonte_entry.grid(row=4, column=1, sticky="w", padx=5)
fonte_entry.insert(0, "A0")

tk.Label(frame, text="Tamanho da fonte (LxA):", bg="#2E2E2E", fg="white").grid(row=5, column=0, sticky="w")
fonte_l_entry = tk.Entry(frame, width=5, bg="#3C3C3C", fg="white")
fonte_l_entry.grid(row=5, column=1, sticky="w", padx=(0, 2))
fonte_l_entry.insert(0, "40")
fonte_h_entry = tk.Entry(frame, width=5, bg="#3C3C3C", fg="white")
fonte_h_entry.grid(row=5, column=1, sticky="e", padx=(2, 0))
fonte_h_entry.insert(0, "40")

# Impressora Zebra

tk.Label(frame, text="IP da impressora:", bg="#2E2E2E", fg="white").grid(row=6, column=0, sticky="w")
ip_entry = tk.Entry(frame, width=15, bg="#3C3C3C", fg="white")
ip_entry.grid(row=6, column=1, sticky="w", padx=5)
ip_entry.insert(0, "192.168.1.100")

tk.Label(frame, text="Porta:", bg="#2E2E2E", fg="white").grid(row=7, column=0, sticky="w")
porta_entry = tk.Entry(frame, width=6, bg="#3C3C3C", fg="white")
porta_entry.grid(row=7, column=1, sticky="w", padx=5)
porta_entry.insert(0, "9100")

enviar_check = tk.IntVar()
tk.Checkbutton(frame, text="Enviar diretamente para a impressora", variable=enviar_check,
               bg="#2E2E2E", fg="white", selectcolor="#2E2E2E").grid(row=8, column=0, columnspan=2, sticky="w")

# Status e preview
status_label = tk.Label(janela, text="Pronto", anchor="w", bg="#2E2E2E", fg="white")
status_label.pack(fill="x", padx=20, pady=5)

preview_frame = tk.LabelFrame(janela, text="Pré-visualização da última etiqueta", bg="#2E2E2E", fg="white")
preview_frame.pack(padx=20, pady=10, fill="both", expand=True)
preview_label = tk.Label(preview_frame, bg="#2E2E2E")
preview_label.pack(padx=10, pady=10)

# Botão principal
tk.Button(janela, text="Gerar Etiquetas", bg="#4CAF50", fg="white", height=2, command=iniciar_geracao).pack(pady=10)

janela.mainloop()
