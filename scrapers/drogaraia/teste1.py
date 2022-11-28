import requests

headers = {
    'authority': 'api-gateway-prod.drogasil.com.br',
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'origin': 'https://www.drogaraia.com.br',
    'referer': 'https://www.drogaraia.com.br/',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
}

response = requests.get('https://api-gateway-prod.drogasil.com.br/search/v2/store/DROGARAIA/channel/SITE/product/search?term=dermage&origin=undefined&p=2&ranking=undefined&facets=&tokenCart=xn8Or8dtsfyU1jwyK6YJyhnaVETvqJUI&limit=36&offset=36&sort_by=relevance:desc', headers=headers).json()
print(response['results'])