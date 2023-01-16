import requests
import locale
import json
from ulid import ULID
from datetime import datetime
from headers_drogariavenancio import headers


drogariacatarinense_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')


def requisicao_drogariacatarinense():
    drogariacatarinense = drogariacatarinense_session.get(
        'https://www.drogariavenancio.com.br/api/catalog_system/pub/products/search?&ft=dermage&PS=24&sl=59e923b8-8598-4b5b-9e5d-e9fef0d71623&cc=24&sm=0&PageNumber=1&_from=0&_to=49', headers=headers).json()
    lista_produtos = [produto for produto in drogariacatarinense]
    return lista_produtos


def buscar_produtos(lista_items):
    links_produtos = [produto['link'] for produto in lista_items]
    lista_produtos = [produto['items'] for produto in lista_items]
    print(lista_produtos, links_produtos)
    return lista_produtos, links_produtos


def data_hora():
    data = datetime.now()
    atual = data.strftime("%d/%m/%Y - %H:%M:%S")
    return atual


def informacoes_produtos():
    info_produtos, links_produtos = buscar_produtos(requisicao_drogariacatarinense())
    DICIO['precos'] = []
    DICIO['lojas'] = [{'id': 9, 'nome': 'Drogaria Venancio',
                      'site': 'https://www.drogariavenancio.com.br'}]
    for produto, link in zip(info_produtos, links_produtos):
        ean, preco = produto[0]['ean'], locale.currency(
            produto[0]['sellers'][0]['commertialOffer']['Price'])
        DICIO['precos'].append(
            {'id': str(ULID()), 'ean_id': ean, 'loja_id': 9, 'preco': preco, 'link': link, 'datahora': data_hora()})
    return DICIO


def criar_json(info):
    with open('JSON/drogariacatarinense.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(informacoes_produtos())


start()
