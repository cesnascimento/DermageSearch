import requests
import json
from bs4 import BeautifulSoup


http = requests.get('https://www.drogaraia.com.br/dermage-shampoo-revicare-prolumi-200ml.html')
soup = BeautifulSoup(http.text, 'html.parser')
doc = soup.find("script", type='application/ld+json').getText()
a = json.loads(doc)
print(a['offers']['price'])