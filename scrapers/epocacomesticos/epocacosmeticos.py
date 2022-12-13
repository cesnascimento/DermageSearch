import requests
import json
import re
from headers_epocacosmeticos import headers
from bs4 import BeautifulSoup


epocacosmeticos_session = requests.Session()
DICIO = {}


def requisicao_epocacosmeticos():
    produtos = list()
    for page in range(1, 8):
        epocacosmeticos = epocacosmeticos_session .get(
            f'https://www.epocacosmeticos.com.br/buscapagina?fq=B%3a2000614&PS=16&sl=152ae237-60f0-45a5-8b6f-1e22515eee63&cc=4&sm=0&PageNumber={page}', headers=headers)
        soup = BeautifulSoup(epocacosmeticos.text, 'html.parser')
        try:
            links = soup.find_all('a', 'shelf-default__link')
            for link in links:
                produtos.append(link['href'])
        except:
            pass
    return produtos

def navegar_produtos(links):
    DICIO['precos'] = []
    DICIO['lojas'] = [
        {'id': 4, 'nome': 'Epoca Cosmeticos', 'site': 'https://www.epocacosmeticos.com.br/'}]
    for num, link in enumerate(links, 202):
        epocacosmeticos = epocacosmeticos_session.get(link)
        soup = BeautifulSoup(epocacosmeticos.text, 'html.parser')
        #product__gallery--sku
        try:
            ean = soup.find('label', 'sku-ean-code').getText()
            preco = soup.find('strong', 'skuBestPrice').getText()
            preco = re.sub(' ', '', preco)
            DICIO['precos'].append(
                {'id': num, 'ean_id': ean, 'loja_id': 4, 'preco': preco, 'link': link})
        except:
            pass
    return DICIO


def criar_json(info):
    with open('JSON/epocacosmeticos.json', 'w') as jsonfile:
        json.dump(info, jsonfile)



def start():
    criar_json(navegar_produtos(requisicao_epocacosmeticos()))


start()