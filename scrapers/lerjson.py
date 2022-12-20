import json

dicio = dict()
with open('JSON/dermage.json', 'r') as f1, open('JSON/drogariacatarinense.json', 'r') as f2, open('JSON/sephora.json', 'r') as f3, open('JSON/epocacosmeticos.json', 'r') as f4, open('JSON/belezanaweb.json', 'r') as f5, open('JSON/drogaraia.json', 'r') as f6, open('JSON/farmagora.json', 'r') as f7:
    f1, f2, f3, f4, f5, f6, f7 = json.load(f1), json.load(f2), json.load(f3), json.load(f4), json.load(f5), json.load(f6), json.load(f7)

    #lojas
    for lojas in f2['lojas']:
        f1['lojas'].append(lojas)
    for lojas in f3['lojas']:
        f1['lojas'].append(lojas)
    for lojas in f4['lojas']:
        f1['lojas'].append(lojas)
    for lojas in f5['lojas']:
        f1['lojas'].append(lojas)
    for lojas in f6['lojas']:
        f1['lojas'].append(lojas)
    for lojas in f7['lojas']:
        f1['lojas'].append(lojas)
    
    #precos
    for precos in f2['precos']:
        f1['precos'].append(precos)
    for precos in f3['precos']:
        f1['precos'].append(precos)
    for precos in f4['precos']:
        f1['precos'].append(precos)
    for precos in f5['precos']:
        f1['precos'].append(precos)
    for precos in f6['precos']:
        f1['precos'].append(precos)
    for precos in f7['precos']:
        f1['precos'].append(precos)

    with open('JSON/geral1.json', 'w') as jsonfile:
        json.dump(f1, jsonfile)