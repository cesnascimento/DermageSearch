import requests
import locale
import json
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
            print(produto)
            produtos.append(produto)
    return produtos


def informacoes_produtos(produtos):
    DICIO['precos'] = []
    DICIO['lojas'] = [
        {'id': 6, 'nome': 'Drogaraia', 'site': 'https://www.drogaraia.com.br/'}]
    for num, produto in enumerate(produtos, 325):
        nome = produto['name']
        ean, preco = produto['ean'], locale.currency(produto['valueTo'])
        print(nome, ean, preco)
        DICIO['precos'].append(
                {'id': num, 'ean_id': ean, 'loja_id': 6, 'preco': preco})
    return DICIO


def criar_json(info):
    with open('JSON/drogaraia.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(informacoes_produtos(buscar_produto()))



start()
