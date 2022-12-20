import requests
from headers_farmagora import headers

for number in range(0, 64, 8):
        responses = requests.get(
            f'https://www.farmagora.com.br/api/catalog_system/pub/products/search?fq=B:2384&PS=24&sl=ba7aedf8-c57e-44a0-ba5c-83285d3577a3&cc=24&sm=0&PageNumber=0&O=OrderByBestDiscountDESC&_from={number}&_to={number+7}', headers=headers,).json()
        for response in responses:
            print(number)
            print(response['productName'])