import requests
import locale
import json
from ulid import ULID
from datetime import datetime
from headers_sephora import headers, params

sephora_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')


def requisicao_sephora():
    produtos = dict()
    for pagina in range(0, 3):
        sephora = sephora_session.get('https://api.linximpulse.com/engage/search/v3/search',
                                      params=params(pagina), headers=headers).json()
        produtos.update(sephora)
    return produtos


def data_hora():
    data = datetime.now()
    atual = data.strftime("%d/%m/%Y - %H:%M:%S")
    return atual

def buscar_produtos(produtos):
    DICIO['precos'] = []
    DICIO['lojas'] = [
        {'id': 3, 'nome': 'Sephora', 'site': 'https://www.sephora.com.br/'}]
    for produto in produtos['products']:
        preco, ean, link = locale.currency(
            produto['price']), produto['skus'][0]['properties']['eanCode'], produto['skus'][0]['properties']['url']
        DICIO['precos'].append(
            {'id': str(ULID()), 'ean_id': ean, 'loja_id': 3, 'preco': preco, 'link': f'https://www.sephora.com.br/{link.replace("/", "")}', 'datahora': data_hora()})
    return DICIO


def criar_json(info):
    with open('../JSON/sephora.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(buscar_produtos(requisicao_sephora()))


start()
