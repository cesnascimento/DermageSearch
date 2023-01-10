import requests
import locale
import json
from ulid import ULID
from datetime import datetime
from headers_drogariasaopaulo import headers, params

drogariasaopaulo_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')



def requisicao_drogariasaopaulo():
    drogariasaopaulo = drogariasaopaulo_session.get('https://api.linximpulse.com/engage/search/v3/search', params=params, headers=headers).json()
    info_skus = [sku for sku in drogariasaopaulo['products']]
    return info_skus


def data_hora():
    data = datetime.now()
    atual = data.strftime("%d/%m/%Y - %H:%M:%S")
    return atual


def informacoes_produtos(skus):
    DICIO['precos'] = []
    DICIO['lojas'] = [{'id': 7, 'nome': 'Drogaria São Paulo',
                      'site': 'https://www.drogariasaopaulo.com.br/'}]
    for sku in skus:
        ean, preco, link =  sku['skus'][0]['properties']['eanCode'], sku['price'], f"https://{sku['url']}"
        DICIO['precos'].append(
            {'id': str(ULID()), 'ean_id': ean, 'loja_id': 7, 'preco': preco, 'link': link, 'datahora': data_hora()})
    
    return DICIO


def criar_json(info):
    with open('../JSON/drogariasaopaulo.json', 'w') as jsonfile:
        json.dump(info, jsonfile)



def start():
    criar_json(informacoes_produtos(requisicao_drogariasaopaulo()))

start()