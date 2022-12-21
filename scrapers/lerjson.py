import json
import os


def folder_jsons():
    files_json = os.listdir('JSON')
    return files_json


def read_json_dermage(files):
    dermage_json = [file for file in files if 'dermage.json' in file]
    return os.path.join('JSON', dermage_json[0])


def open_archive_json(file):
    file = json.load(open(file, 'r'))
    return file


def get_json_geral(files):
    file = [os.path.join('JSON', file)
            for file in files if 'dermage' not in file if 'geral' not in file]
    return file


def build_json(dermage, jsons):
    for json in jsons:
        archive = open_archive_json(json)
        for lojas in archive['lojas']:
            dermage['lojas'].append(lojas)
        for precos in archive['precos']:
            dermage['precos'].append(precos)
    return dermage


def create_json(file):
    with open('JSON/geral.json', 'w') as archive:
        json.dump(file, archive)


def start():
    file_dermage = read_json_dermage(folder_jsons())
    dermage = open_archive_json(file_dermage)
    jsons = get_json_geral(folder_jsons())
    file = build_json(dermage, jsons)
    create_json(file)


start()
