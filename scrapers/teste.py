import json
import os


def folder_jsons():
    files_json = os.listdir('JSON')
    return files_json


def read_json_dermage(files):
    dermage_json = [file for file in files if 'dermage.json' in file]
    return os.path.join('JSON', dermage_json[0])


def open_json_dermage(file):
    file = json.load(open(file, 'r'))
    return file


def get_json_geral(files):
    file = [os.path.join('JSON', file)
            for file in files if 'dermage.json' and 'geral1.json' and 'geral.json' not in file]
    return file


def open_archive(archive):
    archive = json.load(open(archive, 'r'))
    return archive


def build_json(dermage, jsons):
    for json in jsons:
        archive = open_archive(json)
        print(archive['lojas'])
        for lojas in archive['lojas']:
            dermage['lojas'].append(lojas)
        for precos in archive['precos']:
            dermage['precos'].append(precos)
    
    with open('JSON/geral1.json', 'w') as jsonfile:
        json.dump(dermage, jsonfile)


def start():
    file_dermage = read_json_dermage(folder_jsons())
    dermage = open_json_dermage(file_dermage)
    #print(dermage)
    jsons = get_json_geral(folder_jsons())
    file = build_json(dermage, jsons)
    print(file)


start()
