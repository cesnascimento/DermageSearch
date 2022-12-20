import requests
import json
import locale
from datetime import datetime
from headers_farmagora import headers

data = dict()
locale.setlocale(locale.LC_MONETARY, '')


def data_hora():
    data = datetime.now()
    atual = data.strftime("%d/%m/%Y - %H:%M:%S")
    return atual


def requisicao_farmagora():
    data['lojas'] = [
        {'id': 7, 'nome': 'Farmagora', 'site': 'https://www.farmagora.com.br/'}]
    data['precos'] = []
    n = 565
    for number in range(0, 64, 8):
        responses = requests.get(
            f'https://www.farmagora.com.br/api/catalog_system/pub/products/search?fq=B:2384&PS=24&sl=ba7aedf8-c57e-44a0-ba5c-83285d3577a3&cc=24&sm=0&PageNumber=0&O=OrderByBestDiscountDESC&_from={number}&_to={number+7}', headers=headers,).json()
        for response in responses:
            print(response['productName'])
            n += 1
            try:
                preco = response['items'][0]['sellers'][0]['commertialOffer']['Installments'][0]['Value']
                ean, link = response['items'][0]['ean'], response['link']
                data['precos'].append({'id': n, 'ean_id': ean, 'loja_id': 7, 'preco': locale.currency(preco),
                                       'link': f'{link}', 'datahora': data_hora()})
            except:
                pass

    return data


def criar_json(info):
    with open('JSON/farmagora.json', 'w') as jsonfile:
        json.dump(info, jsonfile)


def start():
    criar_json(requisicao_farmagora())


start()
