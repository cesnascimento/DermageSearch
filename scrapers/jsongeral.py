import json
from collections import Counter

dicio1 = {}
dicio2 = {}

with open('JSON/dermage.json', 'r') as f1, open('JSON/drogariacatarinense.json', 'r') as f2, open('JSON/sephora.json', 'r') as f3:
    f1, f2, f3 = json.load(f1), json.load(f2), json.load(f3)
    ini_dictionary1 = Counter(f1)
    ini_dictionary2 = Counter(f2)
    ini_dictionary3 = Counter(f3)
    final_dictionary = {x: ini_dictionary1.get(x, 0) + ini_dictionary2.get(x, 0) + ini_dictionary3.get(x, 0)
                        for x in set(ini_dictionary1).union(ini_dictionary2, ini_dictionary3)}
    with open('JSON/geral.json', 'a') as jsonfile:
        json.dump(final_dictionary, jsonfile)
