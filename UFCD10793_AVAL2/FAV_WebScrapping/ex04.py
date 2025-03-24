'''
Exercício 4 - FAV Enunciado WebScraping - Customização
'''
import re
import requests
from bs4 import BeautifulSoup

from enum import Enum, auto
class DumpToDiskMethod(Enum):
    PANDAS = auto()
    CSV = auto()
#end class

DEBUG = True
DUMP_TO_DISK_METHOD = DumpToDiskMethod.PANDAS


dump_filename = 'eisnt_cursos.csv'

# URL da página de cursos
url = 'https://eisnt.com/'


# Cabeçalhos para simular um Browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html5lib')


# Lista para armazenar os dados dos cursos
scraped_data = []

# Elementos que contêm as informações dos cursos
blocos = soup.find_all('div', class_='borda wpb_column vc_column_container vc_col-sm-3')
for bloco in blocos:
    p_tag = bloco.find('p')
    if not p_tag:
        continue

    #if "Cronograma" not in bloco.get_text():
    #    continue

    texto = p_tag.get_text(separator='\n', strip=True)
    # Extrair dados com expressões regulares
    nome_match = re.search(r'^Curso de (.+)', texto)
    carga_match = re.search(r'Carga horária:\s*(.+)', texto)
    inicio_match = re.search(r'Início previsto:\s*(.+)', texto)
    horario_match = re.search(r'Horário:\s*(.+)', texto)

    cronograma_link = ''
    for a in p_tag.find_all('a', href=True):
        if 'cronogramaAccao' in a['href']:
            cronograma_link = a['href']
            break

    if nome_match and carga_match and inicio_match and horario_match:
        scraped_data.append({
            'Nome do Curso': nome_match.group(1),
            'Carga Horária': carga_match.group(1),
            'Data de Início': inicio_match.group(1),
            'Horário': horario_match.group(1),
            'Link do Cronograma': cronograma_link
        })
    #end if
#end for

if DEBUG: print(scraped_data)

# Salvar os Dados usando Pandas
if DUMP_TO_DISK_METHOD == DumpToDiskMethod.PANDAS:
    import pandas as pd
    df = pd.DataFrame(scraped_data)
    df.to_csv(dump_filename, index=False, encoding='utf-8-sig')
#end if


# Salvar os Dados usando CSV
if DUMP_TO_DISK_METHOD == DumpToDiskMethod.CSV:
    import csv
    with open(dump_filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['Nome do Curso', 'Carga Horária', 'Data de Início', 'Horário', 'Link do Cronograma'])
        writer.writeheader()
        writer.writerows(scraped_data)
    #end with
#end if

