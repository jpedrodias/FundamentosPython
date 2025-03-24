'''
Exercício 4 - FAV Enunciado WebScraping - Customização
'''

import requests
from bs4 import BeautifulSoup

from enum import Enum, auto
class DumpToDiskMethod(Enum):
    PANDAS = auto()
    CSV = auto()
    SQLITE = auto()
#end class

DUMP_TO_DISK_METHOD = DumpToDiskMethod.CSV