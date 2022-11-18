import requests
import re
import json
import locale
from bs4 import BeautifulSoup
from headers_dermage import categorias, headers, params

dermage_session = requests.Session()


def requisicao_dermage():
    for categoria in categorias:
        dermage = dermage_session.get(f'https://www.dermage.com.br/{categoria}', params=params, headers=headers)
        print(dermage)


def start():
    requisicao_dermage()
    #buscar_produtos(requisicao_dermage())


start()


#dermage_session.get(f'https://www.dermage.com.br/{categ}')
#rint(categs)

