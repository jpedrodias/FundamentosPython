'''
Sample 1 - FAV Enunciado ZPL
'''

import os, requests


# change the working directory to the script's directory
workdir = os.path.dirname(os.path.abspath(__file__))
os.chdir(workdir)


zpl = "^XA^F050,50^A0N,50,50^FDOla Mundo!^FS^XZ"
url = "https://api.labelary.com/v1/printers/8dpmm/labels/4x6/0/"

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(url, data=zpl, headers=headers)

filename = 'data/etiqueta.png'

if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
        print("Etiqueta gerada com sucesso.")
else:
    print(f"Erro: {response.status_code}")
    print(response.text)