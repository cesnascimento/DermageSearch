import requests
import re
import json
import locale
from bs4 import BeautifulSoup
from headers_dermage import mount_payload


dermage_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')
categorias = ['rosto', 'corpo', 'cabelo', 'fotoprotecao', 'maquiagem']


def buscar_skus(categoria, num_paginas):
    codigos_skus = list()
    for num_pagina in num_paginas:
        dermage = dermage_session.get(**mount_payload(categoria, num_pagina))
        soup = BeautifulSoup(dermage.text, 'html.parser')
        buscar_skus = [x['data-id'] for x in soup.find_all('span', 'skuProd')]
        for sku in buscar_skus:
           codigos_skus.append(sku)
    return codigos_skus


def listar_skus():
    for categoria in categorias:
        if categoria == 'rosto':
            num_paginas = [x for x in range(1,5)]
            info = buscar_skus(categoria, num_paginas)
            print(info)
            '''for num_pagina in range(1, 5):
                for i in buscar_skus(categoria, num_pagina):
                    print(i)
    todos_skus = list()
    for categoria in categorias:
        if categoria == 'rosto':
            for num_pagina in range(1, 5):
                todos_skus.append(buscar_skus(categoria, num_pagina))
        elif categoria == 'corpo':
            for num_pagina in range(1, 3):
                todos_skus.append(buscar_skus(categoria, num_pagina))
        elif categoria == 'cabelo':
            for num_pagina in range(1, 2):
                todos_skus.append(buscar_skus(categoria, num_pagina))
        elif categoria == 'fotoprotecao':
            for num_pagina in range(1, 2):
                todos_skus.append(buscar_skus(categoria, num_pagina))
        else:
            for num_pagina in range(1, 3):
                todos_skus.append(buscar_skus(categoria, num_pagina))
    return todos_skus'''


def informacoes_produtos(todos_skus):
    pass
    '''for skus in todos_skus:
        dermage_apis = dermage_session.get(f'https://www.dermage.com.br/produto/sku/{skus}')
        print(dermage_apis)
'''


def start():
    informacoes_produtos(listar_skus())


start()
