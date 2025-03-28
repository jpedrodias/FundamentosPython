'''
Sample 2 - FAV Enunciado ZPL
'''
import os, csv, requests

# change the working directory to the script's directory
workdir = os.path.dirname(os.path.abspath(__file__))
os.chdir(workdir)


# Define a pasta de saída
os.makedir('data', exist_ok=True)

# Configuração da impressora e etiqueta
from dataclasses import dataclass

@dataclass
class Settings:
    dpi = '8dpmm'
    size = '4x6'
    rotation = '0'
    labelary_url = f"https://api.labelary.com/v1/printers/{dpi}/labels/{size}/{rotation}/"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}


# Lê os dados do CSV e gera etiquetas

