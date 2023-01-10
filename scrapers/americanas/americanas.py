import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.americanas.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'B2W-PID=1672682372025.0.38702041663678766; B2W-UID=va_1672682372025.0.3733466245668573; _gcl_au=1.1.947252532.1672682373; _px_uAB=MTI4OTV8dHJ1ZQ==; _px_f394gi7Fvmc43dfg_user_id=Mzg1ZDU4ODEtOGFjNy0xMWVkLTk3ZTUtYzM0Y2E4MjExNWRm; __gads=ID=35970ed7d1edd958:T=1672682377:S=ALNI_Ma9WMDyXIqu5DZbVYxm6k2XxHIIaQ; _pxvid=3a62d5ba-8ac7-11ed-a3c4-5a6a4f505666; B2W-SID=1673360153875.0.8305378867470967; mesoRegion=3301; legionRegion=1330023; macroRegion=RJ_CAPITAL; MobileOptOut=1; b2wDevice=eyJvcyI6IldpbmRvd3MgTlQiLCJvc1ZlcnNpb24iOiIxMC4wIiwidmVuZG9yIjoiTWljcm9zb2Z0IiwidHlwZSI6ImRlc2t0b3AiLCJta3ROYW1lIjoiTWljcm9zb2Z0IEVkZ2UgMTA4IiwibW9kZWwiOiJFZGdlIiwibW9iaWxlT3B0T3V0IjoiZmFsc2UifQ==; b2wDeviceType=desktop; searchTestAB=old; b2wChannel=ACOM; B2W-IU=false; cdn-lat=-22.90; cdn-long=-43.23; cdn-country=BR; cdn-region=RJ; cdn-city=RIODEJANEIRO; catalogTestAB=null; _gid=GA1.3.2039344908.1673360155; pxcts=5009ffdf-90f1-11ed-b45c-6d616a766e48; __gpi=UID=000008f0ba69e3c5:T=1672682377:RT=1673360168:S=ALNI_MbCUnebbvsFk4qYWdjDVMYMgnX7EQ; ak_bmsc=7A243E0F850E253C2601216B5C9E4FC8~000000000000000000000000000000~YAAQdbshyUPF7/GEAQAAGmd7nBKTzq+TGQ6vxCpBGmSUD2fMIZAdE+gzFqFFnLFx+OlS+UDvd4vvEnMVDrMgITr7Geb6op7himlIRWNXp2lJu0/fRzho8TQffp9jNV3sHfT191onMXL/nO7x2wqnjSl2no4qnbeOoQ81jGEZow4Vu1DCrZzOlklihjowWUYWKN7uBkBQd+HQoSu0NvE6bfD+44bfLGD1N3iGfnpyIJ9bEdAmt0hA65VerH0JnlNpUIA+M2VP8bmWOSzfuwP1jE8CpHfD2F3HjLNltnfCmgnXBgi9TfVXWLsYFTFnCL1LHgcKSju5Db1vtwTYrHDTPGQSoDYccpFhKBB5xIIDw2N8/8hiWXMGC4ReQxCkLLmDO7VLDd0fl9amAc/c+MOmTGkPhSx+4UzT1XA9/RrfNF13LMe28ez5cAl3oZvWeOpr0tUCtEsxiKB9BriNlgYjfP1P159FuwS8HGgnG6+5JU3IhaAjFplVgolr6ZQB4qUwZdM=; c_privacyPolicy=1; cto_bundle=Jq6RRl85THl6Y0NmRHBSTHZwWjlzMU9RQzEzeFF0MGpSY2olMkZFRUhZSndrVmxzOG9MVVZ5VjA2ejZQd01FYSUyQllsYUlCZ2RwU2Jkelk5OFRFd3pwZFhuWk05M2V1ZHdMWkdvcnRoTG4lMkZQTWJGVm1Ec1pLdHZVUG9KYSUyQlFsb1JBUVdXd2ZGRVVoaUM3UyUyRkpSSEdhbklDYkllaVd3JTNEJTNE; _gat_UA-97626372-1=1; bm_sv=759F9E78EF15AB3B4B93C8ECC5E21AE5~YAAQb7shyRYQqxiFAQAA7nmjnBIpowp+w+84ow/WBaZ6PgRg4HBZqCYKspGKIRJpKDDtwiOoKRfZIz8YEviteQY+8qP0ioC5qgz686K/hvgqjGMjBsiSoWH+kGZ2M6PhNGkz4+Ihqmg8qyGOkknpzsa1gPKux+RRQVK4LQr1TUAhNQ9fmFF0D0fswZ0xISVrenZz/pKpvEVEO9gvCbC+aoSYUJd72V4CfymCr9mYYqO5qVhWgi5JRU70Bi3W/oBuB2V9y9H5Eds=~1; _dd_s=rum=0&expire=1673371138107; _ga=GA1.3.1138867135.1672682373; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _px3=cce33dbdbdfa69cbdf564b23c39e43c5aaa4015d7e36d22478c7292c14d8dee9:ve42kSf26BvwEnZpnxY9q/aHWhoczEu9KunPUkBoeA8EdwPRv1nrU8oywZXosL+w6bbczQS6EmS7OCcONM4X6Q==:1000:kwrDWOJRjNSuWvhlHvzDFL+8KaEqQpD6hd/FzLTvBY4WpQj0v6pv+I3Rd+6LHJnWUUwqUrWFDit05A/Ka478HpjluYg6U0Z7AwMg1zfi+PQzNXRlxoQXTDJOOocNj6R9GStvNs/59XdOyo+Feq9CQneJjxYnJeWdF36/mFAS6C8C1OrtlE2UPTsqfGsyMEUBXTWYEPKLdYSPlsI9W4oPzg==; _px2=eyJ1IjoiYzYzODJlOTAtOTEwOC0xMWVkLTkxNzMtNWIyMmI5MTM5ZDYzIiwidiI6IjNhNjJkNWJhLThhYzctMTFlZC1hM2M0LTVhNmE0ZjUwNTY2NiIsInQiOjE2NzMzNzA1NDA4NDYsImgiOiI2NDhmODQ5MWNhNDYwZDM4ZTQyOTQwNWJkNjkwMDFiYmQ0YTRlZmEyZDg0MGE5NWVmMzk1MDc5NWY2NGM4MDkyIn0=; _ga_DFEPZNP57H=GS1.1.1673367609.6.1.1673370242.55.0.0',
    'if-none-match': 'W/"8b745-hksW9vERrJSYFSL7TM7Woz02zoE"',
    'referer': 'https://www.americanas.com.br/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
}

params = {
    'sortBy': 'higherPriceRelevance',
    'limit': '24',
    'offset': '0',
}

response = requests.get('https://www.americanas.com.br/busca/dermage', params=params, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)