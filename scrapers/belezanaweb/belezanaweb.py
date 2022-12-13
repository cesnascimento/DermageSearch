import requests
import json
import locale
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

def buscar_produtos(links_produtos):
    DICIO['precos'] = []
    DICIO['lojas'] = [
        {'id': 5, 'nome': 'Belezanaweb', 'site': 'https://www.belezanaweb.com.br/'}]
    for num, link_produto in enumerate(links_produtos, 278):
        belezanaweb = belezanaweb_session.get(link_produto['href'], headers=headers)
        soup = BeautifulSoup(belezanaweb.text, 'html.parser')
        info_produtos = json.loads(soup.find('script', type='application/ld+json').string)
        for produto in info_produtos:
            ean, preco = produto['gtin'], locale.currency(float(produto['offers']['highPrice']))
            DICIO['precos'].append(
            {'id': num, 'ean_id': ean, 'loja_id': 5, 'preco': preco, 'link': link_produto['href']})
    print(DICIO)
    return DICIO


def criar_json(info):
    with open('JSON/belezanaweb.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(buscar_produtos(requisicao_belezanaweb()))

start()
