'''
Exercício 4 - FAV Enunciado WebScraping - FlaskApp
'''
from flask import Flask, render_template, request

import re
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
def index():
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

    return render_template('index.html', cursos=scraped_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)