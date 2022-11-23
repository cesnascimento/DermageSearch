from headers_drogariacatarinense import headers
import requests
import locale
import json


drogariacatarinense_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')


def requisicao_drogariacatarinense():
    drogariacatarinense = drogariacatarinense_session.get(
        'https://www.drogariacatarinense.com.br/api/catalog_system/pub/products/search?&ft=dermage&PS=24&sl=59e923b8-8598-4b5b-9e5d-e9fef0d71623&cc=24&sm=0&PageNumber=1&_from=0&_to=49', headers=headers).json()
    lista_produtos = [produto['items'] for produto in drogariacatarinense]
    return lista_produtos


def buscar_produtos(lista_items):
    lista_produtos = [produto for produto in lista_items]
    return lista_produtos


def informacoes_produtos():
    info_produtos = buscar_produtos(requisicao_drogariacatarinense())
    DICIO['produtos'], DICIO['precos'], DICIO['lojas'] = [], [], []
    DICIO['lojas'].append(
        {'id': 2, 'nome': 'Drogaria Catarinense', 'site': headers['authority']})
    for num, produto in enumerate(info_produtos, 1):
        nome, ean = produto[0]['name'], produto[0]['ean']
        preco = locale.currency(
            produto[0]['sellers'][0]['commertialOffer']['Price'])
        DICIO['produtos'].append({'nome': nome, 'ean': ean})
        DICIO['precos'].append(
            {'id': num, 'ean_id': ean, 'loja_id': 2, 'preco': preco})
    return DICIO


def criar_json(info):
    with open('JSON/drogariacatarinense.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(informacoes_produtos())


start()