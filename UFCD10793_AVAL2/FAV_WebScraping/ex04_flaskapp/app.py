'''
Exercício 4 - FAV Enunciado WebScraping - FlaskApp
'''
# Standard Libraries
import re
from datetime import datetime, timedelta, timezone

from flask import Flask, render_template, request, redirect, url_for, send_file, abort
from flask_sqlalchemy import SQLAlchemy

import requests
from bs4 import BeautifulSoup

from os import chdir, getcwd, path
workdir = path.dirname(path.abspath(__file__))
chdir(workdir)

DATABASE_FILE = 'cursos_eisnt.sqlite'
DATABASE_PATH = path.join(workdir, DATABASE_FILE)

db = SQLAlchemy()


# Database Model
class ScrapedEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    # relação um para muitos com Course
    courses = db.relationship('Course', backref='scraped_event', lazy=True)

class UniqueCourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    carga_horaria = db.Column(db.String(50), nullable=False)
    data_inicio = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    cronograma_link = db.Column(db.String(200), nullable=False)

    # Cursos associados a este curso único
    appearances = db.relationship('Course', backref='unique_course', lazy=True)
    
    def __repr__(self):
        return f'<UniqueCourse {self.nome}>'
    
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_course_id = db.Column(db.Integer, db.ForeignKey('unique_course.id'), nullable=False)
    scraped_event_id = db.Column(db.Integer, db.ForeignKey('scraped_event.id'), nullable=False)


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'very secret key - this is the salt used to encrypt the session'
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = path.join(workdir, 'session')
    SESSION_FILE_THRESHOLD = 100 

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()



def get_data_from_website():
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
    return scraped_data

@app.route('/', methods=['GET', 'POST'])
def index():

    need_download = False
    if request.method == 'POST':
        action = request.form.get('action', 'None')
        if action == 'forcedownload':
            need_download = True
        elif action == 'cleardb':
            db.drop_all()
            db.create_all()
            db.session.commit()
            return redirect(url_for('index'))

    if not need_download:
        web_scraping = ScrapedEvent.query.order_by(ScrapedEvent.data.desc()).first()
        if web_scraping is None:
            need_download = True

        elif datetime.utcnow() - web_scraping.data > timedelta(days=1):
            need_download = True
    
    if need_download:
        web_scraping = ScrapedEvent()
        db.session.add(web_scraping)
        db.session.commit()

        scraped_data = get_data_from_website()
        for course in scraped_data:
            unique = UniqueCourse.query.filter_by(
                nome=course['Nome do Curso'],
                carga_horaria=course['Carga Horária'],
                data_inicio=course['Data de Início'],
                horario=course['Horário'],
                cronograma_link=course['Link do Cronograma']
            ).first()

            if unique is None:
                unique = UniqueCourse(
                    nome=course['Nome do Curso'],
                    carga_horaria=course['Carga Horária'],
                    data_inicio=course['Data de Início'],
                    horario=course['Horário'],
                    cronograma_link=course['Link do Cronograma']
                )
                db.session.add(unique)
                db.session.commit()  # garantir que temos o ID

            new_course = Course(
                unique_course_id=unique.id,
                scraped_event_id=web_scraping.id
            )
            db.session.add(new_course)
        db.session.commit()
    
    
    scraped_data = Course.query.filter_by(scraped_event_id=web_scraping.id).all()
    cursos = []
    for course in scraped_data:
        cursos.append({
            'Nome do Curso': course.unique_course.nome,
            'Carga Horária': course.unique_course.carga_horaria,
            'Data de Início': course.unique_course.data_inicio,
            'Horário': course.unique_course.horario,
            'Link do Cronograma': course.unique_course.cronograma_link
        })

    last_scrap = web_scraping.data.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', cursos=cursos, last_scrap = last_scrap)


@app.route('/download/<filename>')
def download(filename=None):

    data = []
    events = ScrapedEvent.query.order_by(ScrapedEvent.data.desc()).all()
    for event in events:
        for course in event.courses:
            uc = course.unique_course
            data.append({
                'Scraped Event ID': event.id,
                'Scraped Date (UTC)': event.data.strftime('%Y-%m-%d %H:%M:%S'),
                'Course ID': uc.id,
                'Nome do Curso': uc.nome,
                'Carga Horária': uc.carga_horaria,
                'Data de Início': uc.data_inicio,
                'Horário': uc.horario,
                'Link do Cronograma': uc.cronograma_link
            })

    from io import StringIO, BytesIO
    if filename.endswith('.csv'):
        import csv
        output_text  = StringIO()
        writer = csv.DictWriter(output_text, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        output_text .seek(0)
        output = BytesIO(output_text.read().encode('utf-8'))
        output.seek(0)
        return send_file(
            output,
            mimetype='text/csv',
            as_attachment=True,
            download_name=filename
        )
    elif filename.endswith('.json'):
        import json
        output_text  = StringIO()
        json.dump(data, output_text , indent=2, ensure_ascii=False)
        output_text .seek(0)

        output = BytesIO(output_text.read().encode('utf-8'))
        output.seek(0)

        return send_file(
            output,
            mimetype='application/json',
            as_attachment=True,
            download_name=filename
        )
    elif filename.endswith('.xlsx'):
        import pandas as pd
        df = pd.DataFrame(data)
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Cursos')
        output.seek(0)
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )
    else:
        abort(400, description='Formato de ficheiro não suportado. Usa .csv, .json ou .xlsx.')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)