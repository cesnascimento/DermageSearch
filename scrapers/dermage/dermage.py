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


def paginas_in_categorias(nome_categoria):
    if nome_categoria in paginas_categorias.keys():
        num_paginas = [num for num in range(
            1, paginas_categorias[nome_categoria])]
        return num_paginas


def listar_codigos_skus():
    codigos_skus = list()
    for categoria in paginas_categorias.keys():
        num_paginas = paginas_in_categorias(categoria)
        for i in requisicao_dermage(categoria, num_paginas):
                codigos_skus.append(i)
    return list(set(codigos_skus))


def data_hora():
    data = datetime.now()
    atual = data.strftime("%d/%m/%Y - %H:%M:%S")
    return atual


def informacoes_produtos(codigos_skus):
    DICIO['produtos'], DICIO['precos'] = [], []
    DICIO['lojas'] = [
        {'id': 1, 'nome': 'Dermage', 'site': 'htttps://www.dermage.com.br'}]
    num = 0
    for codigo_sku in codigos_skus:
        produtos = dermage_session.get(
            f'https://www.dermage.com.br/produto/sku/{codigo_sku}').json()
        for produto in produtos:
            if re.search('78953891', produto['Ean']):
                num += 1
                ean, nome, preco = produto['Ean'], produto['Name'], locale.currency(
                    produto['SkuSellersInformation'][0]['Price'])
                DICIO['produtos'].append({'nome': nome, 'ean': ean})
                DICIO['precos'].append(
                    {'id': num, 'ean_id': ean, 'loja_id': 1, 'preco': preco, 'datahora': data_hora()})
    return DICIO


def criar_json(info):
    with open('JSON/dermage.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(criar_json(informacoes_produtos(listar_codigos_skus())))


start()
