import requests
import re
import json
import locale
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from headers_dermage import mount_payload, paginas_categorias


dermage_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')


def requisicao_dermage(categoria, num_paginas=2):
    codigos_skus = list()
    for num_pagina in num_paginas:
        dermage = dermage_session.get(**mount_payload(categoria, num_pagina))
        soup = BeautifulSoup(dermage.text, 'html.parser')
        buscar_skus = [x['data-id']
                       for x in soup.find_all('span', 'skuProd')]
        with ThreadPoolExecutor(max_workers=10) as executor:
            for sku in buscar_skus:
                executor.map(codigos_skus.append(sku))
    return codigos_skus


def start():
    requisicao_dermage('rosto', 5)


start()