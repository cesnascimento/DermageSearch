import requests
import json
from headers_farmagora import headers, params


'''def params_page(num):
    for num in range(num, 12, 12)'''

n = 0
for num in range(0,48,12):
    response = requests.get('https://searches.smarthint.co/v5/Search/GetPrimarySearch', params=params(num), headers=headers)
    http = response.text.replace('jQuery18306654931854904724_1670931902596(', '').replace(')', '')
    a = json.loads(http)
    f = json.loads(a[0])
    for produtos in f['Products']:
        n+=1
        print(n, produtos['Title'])