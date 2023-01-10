import requests
import json
import locale
from ulid import ULID
from datetime import datetime
from bs4 import BeautifulSoup
from headers_belezanweb import headers

belezanaweb_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')

def requisicao_belezanaweb():
    belezanaweb = belezanaweb_session.get(
        f'https://www.belezanaweb.com.br/dermage?tab=produtos', headers=headers)
    soup = BeautifulSoup(belezanaweb.text, 'html.parser')
    links_produtos = soup.findAll('a', 'showcase-item-image')
    return list(set(links_produtos))


def data_hora():
    data = datetime.now()
    atual = data.strftime("%d/%m/%Y - %H:%M:%S")
    return atual


def buscar_produtos(links_produtos):
    DICIO['precos'] = []
    DICIO['lojas'] = [
        {'id': 5, 'nome': 'Belezanaweb', 'site': 'https://www.belezanaweb.com.br/'}]
    for link_produto in links_produtos:
        belezanaweb = belezanaweb_session.get(link_produto['href'], headers=headers)
        soup = BeautifulSoup(belezanaweb.text, 'html.parser')
        info_produtos = json.loads(soup.find('script', type='application/ld+json').string)
        for produto in info_produtos:
            ean, preco = produto['gtin'], locale.currency(float(produto['offers']['highPrice']))
            DICIO['precos'].append(
            {'id': str(ULID()), 'ean_id': ean, 'loja_id': 5, 'preco': preco, 'link': link_produto['href'], 'datahora': data_hora()})
    print(DICIO)
    return DICIO


def criar_json(info):
    with open('../JSON/belezanaweb.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(buscar_produtos(requisicao_belezanaweb()))

start()
