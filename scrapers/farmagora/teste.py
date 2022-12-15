import requests

cookies = {
    'VtexRCMacIdv7': 'd3e4feee-8287-496f-8474-5876eaff22f2',
    '_gcl_au': '1.1.1088893066.1666359839',
    'blueID': '81b0f342-3425-4eca-b13c-8c35c5af39ab',
    'checkout.vtex.com': '__ofid=6b3148497a944625b6110ef2b8f75708',
    '.ASPXAUTH': '89864DA1957EDD4468B41E1C0E4D9095D08F3CF9D5814089F31DA54DD3A6A9A60252AD4CACB542A7242B9754210ED37073BBDA54D86B23241218DEAF5CCBB48325F88CA13FD3BF7EB0ABAF5E8D60982749C0E6748E8BE504A3ACCA4BAF1C52F1706F024156697BA9AEC702C6D9F219CA438FB5B628BB4264B49C12820ADA75811593649C85B4CEF090633D68F2A6E74948A594402AC0C8FDEAFB6CBB6C413C25A7D887E7',
    '_fbp': 'fb.2.1666359841088.1319359227',
    '__kdtv': 't%3D1666359842983%3Bi%3D6347e579ba4cd014166c2b9ee53dec9272ef9703',
    '_kdt': '%7B%22t%22%3A1666359842983%2C%22i%22%3A%226347e579ba4cd014166c2b9ee53dec9272ef9703%22%7D',
    'SmartHint-AnonymousConsumer': '973b2728-89db-4e81-b2d3-2ffdae13ac8b',
    'analytic_id': '1666359850383597',
    '_lf': '{%22lm%22:false%2C%22_ga%22:%2267a40015-f1fc-da08-a743-26929fff2b9f%22}',
    'SmartHint-LastSearchsArray': '%5Bnull%5D',
    'voxusmediamanager_acs': 'true',
    '_enviou.com-ca': '{%22tk%22:%2219082022063949ZTT%22}',
    'vtex_segment': 'eyJjYW1wYWlnbnMiOm51bGwsImNoYW5uZWwiOiIxIiwicHJpY2VUYWJsZXMiOm51bGwsInJlZ2lvbklkIjpudWxsLCJ1dG1fY2FtcGFpZ24iOm51bGwsInV0bV9zb3VyY2UiOm51bGwsInV0bWlfY2FtcGFpZ24iOm51bGwsImN1cnJlbmN5Q29kZSI6IkJSTCIsImN1cnJlbmN5U3ltYm9sIjoiUiQiLCJjb3VudHJ5Q29kZSI6IkJSQSIsImN1bHR1cmVJbmZvIjoicHQtQlIiLCJjaGFubmVsUHJpdmFjeSI6InB1YmxpYyJ9',
    'OptanonAlertBoxClosed': '2022-12-13T11:38:11.346Z',
    'VTEXSC': 'sc=1',
    'vtex_session': 'eyJhbGciOiJFUzI1NiIsImtpZCI6IkExNTRERDUzRDNEMzREQUNDQzc3QTJGNTM1ODIyOTUwNDI2MkZENjciLCJ0eXAiOiJqd3QifQ.eyJhY2NvdW50LmlkIjoiYWNiODRmY2ItYjJjYS00OGNkLWE4MGMtZjIyZGNmNjU0MTNiIiwiaWQiOiIyYzQ1OTU4NS04MjJkLTQyMWItOWYyNi0zNjRhOGNlYzdlMzIiLCJ2ZXJzaW9uIjoyLCJzdWIiOiJzZXNzaW9uIiwiYWNjb3VudCI6InNlc3Npb24iLCJleHAiOjE2NzE3Mjg2MTksImlhdCI6MTY3MTAzNzQxOSwiaXNzIjoidG9rZW4tZW1pdHRlciIsImp0aSI6IjFmODE4YWI1LTRlOTMtNDRhMy05OGQzLWI1ZDI1MTI2OTc3NyJ9.NRX-aSBW7mOyZ-Z8o7tThi7exRKFgOrJKy0ls3kszz4Yi9yrrJGUYbfM1vtvkKYzcM4gAc6ccLwjZlDigDztng',
    '_gid': 'GA1.3.1981564619.1671037420',
    'ISSMB': 'ScreenMedia=0&UserAcceptMobile=False',
    'SGTS': 'D4ED5E1557B5796D1F35A995672588D0',
    'voxusmediamanager_id': '16663502901490.495427066778528559udic3jo3ua',
    'orderFormIdSHdone': '6b3148497a944625b6110ef2b8f75708',
    'orderFormIdSH': '6b3148497a944625b6110ef2b8f75708',
    '_lfi': '3',
    '_lfe': '3',
    '_ga': 'GA1.1.175368601.1666359839',
    'urlLastSearch': 'http://www.farmagora.com.br/dermagehttp://www.farmagora.com.br/dermage',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Dec+15+2022+09%3A22%3A01+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=6.38.0&isIABGlobal=false&hosts=&consentId=768b3c8b-bfe2-4a16-86a2-eaaf560e85d1&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=%3B',
    'janus_sid': '50b1f782-efc5-4b4a-8f1b-e5e762bb5a39',
    'AvantiSearchQuery': '{%22route%22:%22/buscapagina%22%2C%22query%22:{%22fq%22:[%22B:2384%22]%2C%22PS%22:%2224%22%2C%22sl%22:%22ba7aedf8-c57e-44a0-ba5c-83285d3577a3%22%2C%22cc%22:%2224%22%2C%22sm%22:%220%22%2C%22PageNumber%22:1%2C%22O%22:%22OrderByBestDiscountDESC%22}%2C%22url%22:%22/buscapagina?fq=B:2384&PS=24&sl=ba7aedf8-c57e-44a0-ba5c-83285d3577a3&cc=24&sm=0&PageNumber=1&O=OrderByBestDiscountDESC%22%2C%22path%22:%22/dermage%22}',
    '_ga_S9ZG3GF87Q': 'GS1.1.1671110129.9.0.1671110129.0.0.0',
    'VtexRCSessionIdv7': 'd2b23856-c822-457c-b1e5-5d41454b92f7',
}

headers = {
    'authority': 'www.farmagora.com.br',
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'VtexRCMacIdv7=d3e4feee-8287-496f-8474-5876eaff22f2; _gcl_au=1.1.1088893066.1666359839; blueID=81b0f342-3425-4eca-b13c-8c35c5af39ab; checkout.vtex.com=__ofid=6b3148497a944625b6110ef2b8f75708; .ASPXAUTH=89864DA1957EDD4468B41E1C0E4D9095D08F3CF9D5814089F31DA54DD3A6A9A60252AD4CACB542A7242B9754210ED37073BBDA54D86B23241218DEAF5CCBB48325F88CA13FD3BF7EB0ABAF5E8D60982749C0E6748E8BE504A3ACCA4BAF1C52F1706F024156697BA9AEC702C6D9F219CA438FB5B628BB4264B49C12820ADA75811593649C85B4CEF090633D68F2A6E74948A594402AC0C8FDEAFB6CBB6C413C25A7D887E7; _fbp=fb.2.1666359841088.1319359227; __kdtv=t%3D1666359842983%3Bi%3D6347e579ba4cd014166c2b9ee53dec9272ef9703; _kdt=%7B%22t%22%3A1666359842983%2C%22i%22%3A%226347e579ba4cd014166c2b9ee53dec9272ef9703%22%7D; SmartHint-AnonymousConsumer=973b2728-89db-4e81-b2d3-2ffdae13ac8b; analytic_id=1666359850383597; _lf={%22lm%22:false%2C%22_ga%22:%2267a40015-f1fc-da08-a743-26929fff2b9f%22}; SmartHint-LastSearchsArray=%5Bnull%5D; voxusmediamanager_acs=true; _enviou.com-ca={%22tk%22:%2219082022063949ZTT%22}; vtex_segment=eyJjYW1wYWlnbnMiOm51bGwsImNoYW5uZWwiOiIxIiwicHJpY2VUYWJsZXMiOm51bGwsInJlZ2lvbklkIjpudWxsLCJ1dG1fY2FtcGFpZ24iOm51bGwsInV0bV9zb3VyY2UiOm51bGwsInV0bWlfY2FtcGFpZ24iOm51bGwsImN1cnJlbmN5Q29kZSI6IkJSTCIsImN1cnJlbmN5U3ltYm9sIjoiUiQiLCJjb3VudHJ5Q29kZSI6IkJSQSIsImN1bHR1cmVJbmZvIjoicHQtQlIiLCJjaGFubmVsUHJpdmFjeSI6InB1YmxpYyJ9; OptanonAlertBoxClosed=2022-12-13T11:38:11.346Z; VTEXSC=sc=1; vtex_session=eyJhbGciOiJFUzI1NiIsImtpZCI6IkExNTRERDUzRDNEMzREQUNDQzc3QTJGNTM1ODIyOTUwNDI2MkZENjciLCJ0eXAiOiJqd3QifQ.eyJhY2NvdW50LmlkIjoiYWNiODRmY2ItYjJjYS00OGNkLWE4MGMtZjIyZGNmNjU0MTNiIiwiaWQiOiIyYzQ1OTU4NS04MjJkLTQyMWItOWYyNi0zNjRhOGNlYzdlMzIiLCJ2ZXJzaW9uIjoyLCJzdWIiOiJzZXNzaW9uIiwiYWNjb3VudCI6InNlc3Npb24iLCJleHAiOjE2NzE3Mjg2MTksImlhdCI6MTY3MTAzNzQxOSwiaXNzIjoidG9rZW4tZW1pdHRlciIsImp0aSI6IjFmODE4YWI1LTRlOTMtNDRhMy05OGQzLWI1ZDI1MTI2OTc3NyJ9.NRX-aSBW7mOyZ-Z8o7tThi7exRKFgOrJKy0ls3kszz4Yi9yrrJGUYbfM1vtvkKYzcM4gAc6ccLwjZlDigDztng; _gid=GA1.3.1981564619.1671037420; ISSMB=ScreenMedia=0&UserAcceptMobile=False; SGTS=D4ED5E1557B5796D1F35A995672588D0; voxusmediamanager_id=16663502901490.495427066778528559udic3jo3ua; orderFormIdSHdone=6b3148497a944625b6110ef2b8f75708; orderFormIdSH=6b3148497a944625b6110ef2b8f75708; _lfi=3; _lfe=3; _ga=GA1.1.175368601.1666359839; urlLastSearch=http://www.farmagora.com.br/dermagehttp://www.farmagora.com.br/dermage; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+15+2022+09%3A22%3A01+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=6.38.0&isIABGlobal=false&hosts=&consentId=768b3c8b-bfe2-4a16-86a2-eaaf560e85d1&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=%3B; janus_sid=50b1f782-efc5-4b4a-8f1b-e5e762bb5a39; AvantiSearchQuery={%22route%22:%22/buscapagina%22%2C%22query%22:{%22fq%22:[%22B:2384%22]%2C%22PS%22:%2224%22%2C%22sl%22:%22ba7aedf8-c57e-44a0-ba5c-83285d3577a3%22%2C%22cc%22:%2224%22%2C%22sm%22:%220%22%2C%22PageNumber%22:1%2C%22O%22:%22OrderByBestDiscountDESC%22}%2C%22url%22:%22/buscapagina?fq=B:2384&PS=24&sl=ba7aedf8-c57e-44a0-ba5c-83285d3577a3&cc=24&sm=0&PageNumber=1&O=OrderByBestDiscountDESC%22%2C%22path%22:%22/dermage%22}; _ga_S9ZG3GF87Q=GS1.1.1671110129.9.0.1671110129.0.0.0; VtexRCSessionIdv7=d2b23856-c822-457c-b1e5-5d41454b92f7',
    'referer': 'https://www.farmagora.com.br/dermage',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get(
    'https://www.farmagora.com.br/api/catalog_system/pub/products/search?fq=B:2384&PS=24&sl=ba7aedf8-c57e-44a0-ba5c-83285d3577a3&cc=24&sm=0&PageNumber=0&O=OrderByBestDiscountDESC&_from=0&_to=6',
    cookies=cookies,
    headers=headers,
).json()
for n, produto in enumerate(response):
    print(n, produto['productName'])