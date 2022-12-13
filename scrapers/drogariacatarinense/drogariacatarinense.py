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
    lista_produtos = [produto for produto in drogariacatarinense]
    return lista_produtos


def buscar_produtos(lista_items):
    links_produtos = [produto['link'] for produto in lista_items]
    lista_produtos = [produto['items'] for produto in lista_items]
    print(lista_produtos, links_produtos)
    return lista_produtos, links_produtos


def informacoes_produtos():
    info_produtos, links_produtos = buscar_produtos(requisicao_drogariacatarinense())
    DICIO['precos'] = []
    DICIO['lojas'] = [{'id': 2, 'nome': 'Drogaria Catarinense',
                      'site': 'https://www.drogariacatarinense.com.br'}]
    for num, (produto, link) in enumerate(zip(info_produtos, links_produtos)):
        ean, preco = produto[0]['ean'], locale.currency(
            produto[0]['sellers'][0]['commertialOffer']['Price'])
        DICIO['precos'].append(
            {'id': num, 'ean_id': ean, 'loja_id': 2, 'preco': preco, 'link': link})
    return DICIO


def criar_json(info):
    with open('JSON/drogariacatarinense.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(informacoes_produtos())


start()
