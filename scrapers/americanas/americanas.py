import requests
from header_americanas import headers, params

response = requests.get(
    'https://mars-v1-americanas-npf.b2w.io/rrserver/api/rrPlatform/recsForPlacements',
    params=params,
    headers=headers,
).json()

for produtos in response['placements']:
    for produto in produtos['recommendedProducts']:
        print(produto['productURL'])