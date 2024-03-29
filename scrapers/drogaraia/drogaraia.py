import requests
import locale
import json
from bs4 import BeautifulSoup
import re
from ulid import ULID
from datetime import datetime
from headers_drogaraia import headers, params
from concurrent.futures import ThreadPoolExecutor


drogaraia_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')


def requisicao_drogaraia(pagina, offset):
    drogaraia = drogaraia_session.get(f'https://api-gateway-prod.drogasil.com.br/search/v2/store/DROGARAIA/channel/SITE/product/search?term=dermage&origin=undefined&ranking=undefined&facets=&tokenCart=xn8Or8dtsfyU1jwyK6YJyhnaVETvqJUI&limit=48&sort_by=price:asc',
                                      headers=headers, params=params(pagina, offset)).json()['results']['products']
    return drogaraia


def offset_paginas(pagina):
    if pagina == 1:
        return 24
    elif pagina == 2:
        return 48
    elif pagina == 3:
        return 96
    elif pagina == 4:
        return 144
    elif pagina == 5:
        return 192
    else:
        if pagina == 6:
            return 240


def buscar_produto():
    produtos = list()
    for pagina in range(1, 7):
        offset = offset_paginas(pagina)
        drogaraia = requisicao_drogaraia(pagina, offset)
        for produto in drogaraia:
            produtos.append(produto)
    return produtos


def data_hora():
    data = datetime.now()
    atual = data.strftime("%d/%m/%Y - %H:%M:%S")
    return atual


def get_name_marketplace(link):
    http = requests.get(link)
    soup = BeautifulSoup(http.text, 'html.parser')
    try:
        market = soup.find('p', attrs={'data-testid': True}).getText()
        market = re.sub('Vendido e entregue por', '', market).strip()
        preco = json.loads(soup.find("script", type='application/ld+json').getText())['offers']['price']
        return market, preco
    except:
        pass


def informacoes_produtos(produtos):
    DICIO['precos'] = []
    DICIO['lojas'] = [
        {'id': 5, 'nome': 'Drogaraia', 'site': 'https://www.drogaraia.com.br/'}]
    for produto in produtos:
        nome = produto['name']
        ean, link = produto['ean'], produto['urlKey'].replace('//', 'https://')
        try:
            market, preco = get_name_marketplace(link)
            preco = locale.currency(float(preco))
            print(nome, ean, link, preco)
            DICIO['precos'].append(
                {'id': str(ULID()), 'ean_id': ean, 'loja_id': 5, 'preco': preco, 'link': link, 'datahora': data_hora(), 'market': f'{market}'})
        except:
            pass
    return DICIO


def criar_json(info):
    with open('../JSON/drogaraia.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(informacoes_produtos(buscar_produto()))


start()
