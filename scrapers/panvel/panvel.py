import requests
import locale
import json
from datetime import datetime
from ulid import ULID
from headers_panvel import headers, json_data, cookies

panvel_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')


def requisicao_panvel():
    response = [panvel_session.post('https://www.panvel.com/api/v2/search',
                                    cookies=cookies, headers=headers, json=json_data(page)).json()['items'] for page in range(1, 5)]
    return response


def navegar_panvel(produtos):
    info = [info for produto in produtos for info in produto]
    return info


def data_hora():
    data = datetime.now()
    atual = data.strftime("%d/%m/%Y - %H:%M:%S")
    return atual


def informacao_produto(infos):
    DICIO['precos'] = []
    DICIO['lojas'] = [
        {'id': 10, 'nome': 'Panvel', 'site': 'https://www.panvel.com'}]
    for info in infos:
        print(info)
        panvel_code = info['panvelCode']
        panvel = panvel_session.get(
            f'https://www.panvel.com/api/v2/catalog/{panvel_code}?uf=RS', cookies=cookies, headers=headers).json()
        ean, preco, link = panvel['ean'], locale.currency(
            panvel['discount']['dealPrice']), f'''https://www.panvel.com/{panvel['link']}'''
        DICIO['precos'].append(
            {'id': str(ULID()), 'ean_id': ean, 'loja_id': 10, 'preco': preco, 'link': link, 'datahora': data_hora()})
    
    return DICIO


def criar_json(info):
    with open('../JSON/panvel.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(informacao_produto(navegar_panvel(requisicao_panvel())))


start()


# api: https://www.panvel.com/api/v2/catalog/601010?uf=RS
