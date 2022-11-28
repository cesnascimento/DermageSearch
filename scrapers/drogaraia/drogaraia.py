import requests
import locale
from headers_drogaraia import headers, params



drogaraia_session = requests.Session()
DICIO = {}
locale.setlocale(locale.LC_MONETARY, '')



def requisicao_drogaraia():
    produtos = dict()
    for paginas in range(1,13):
        for offset in range(12,265):
            if offset % 12 == 0:
                drogaraia = drogaraia_session.get(f'https://api-gateway-prod.drogasil.com.br/search/v2/store/DROGARAIA/channel/SITE/product/search/live?term=dermage&origin=undefined&ranking=undefined&facets=&tokenCart=xn8Or8dtsfyU1jwyK6YJyhnaVETvqJUI&sort_by=relevance:desc', headers=headers, params=params(paginas, offset)).json()
                produtos.update(drogaraia['results'])
    return produtos


def informacao_produto(produto):
    print(produto)


def start():
    print(requisicao_drogaraia(requisicao_drogaraia()))


start()
