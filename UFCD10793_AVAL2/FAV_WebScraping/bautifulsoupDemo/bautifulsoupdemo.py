'''
Exercício 1 - FAV Enunciado WebScraping - BeautifulSoup
'''
import requests
from bs4 import BeautifulSoup


from enum import Enum, auto
class DumpToDiskMethod(Enum):
    PANDAS = auto()
    CSV = auto()
    SQLITE = auto()

#DUMP_TO_DISK_METHOD = DumpToDiskMethod.PANDAS
DUMP_TO_DISK_METHOD = DumpToDiskMethod.CSV


dump_filename = 'temperaturas.csv'

url = 'https://www.accuweather.com'

headers = {
    'User-Agent': 'Mozilla/5.0 /Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

data = []

for mainrow in soup.findAll('div', attrs = {'class': ['nearby-locations-list'] }):
    #print(mainrow)
    for row in mainrow.findAll('a', attrs = {'class': ['nearby-location weather-card'] }):
        #print(row)
        if not row:
            continue
        location = row.find('span', attrs = {'class': ['text title no-wrap'] }).get_text().strip()
        temperature = row.find('span', attrs = {'class': ['text temp'] }).get_text().strip()
        #print(location, temperature)

        data.append(
            {
                'location': location,
                'temperature': temperature
            }
        )
    #end row
#end mainrow

# Salvar os Dados usando Pandas
if DUMP_TO_DISK_METHOD == DumpToDiskMethod.PANDAS:
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(dump_filename, index=False, encoding='utf-8-sig')
#end if

# Salvar os Dados usando CSV
if DUMP_TO_DISK_METHOD == DumpToDiskMethod.CSV:
    import csv
    with open(dump_filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['location', 'temperature'])
        writer.writeheader()
        writer.writerows(data)
    #end with
#end if