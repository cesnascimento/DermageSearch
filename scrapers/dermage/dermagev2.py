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


def requisicao_dermage(categoria, num_paginas):
    lista_skus = list()
    for pagina in num_paginas:
        dermage = dermage_session.get(**mount_payload(categoria, pagina))
        soup = BeautifulSoup(dermage.text, 'html.parser')
        buscar_skus = [x['data-id']
                       for x in soup.find_all('span', 'skuProd')]
        lista_skus = lista_skus + buscar_skus
    return lista_skus


def paginas_in_categorias(nome_categoria):
    if nome_categoria in paginas_categorias.keys():
        num_paginas = [num for num in range(
            1, paginas_categorias[nome_categoria])]
        print(num_paginas)
        return num_paginas


def nav_codigos_skus():
    pass


def start():
    requisicao_dermage('rosto', range(0,5))

start()