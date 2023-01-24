import json
import os
from O365 import Account, Connection, FileSystemTokenBackend


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


def alert_price(dermage, files):
    for json_file in files:
        with open(f'{json_file}', 'r') as file:
            for f in file:
                print(file)
                archives = json.loads(f)
                for name, price_dermage in zip(dermage['produtos'], dermage['precos']):
                    for price_file in archives['precos']:
                        if price_dermage['ean_id'] == price_file['ean_id']:
                            a,b = price_dermage['preco'].replace('R$','').replace(',', '.'), price_file['preco'].replace('R$','').replace(',', '.')
                            if abs(float(a) - (float(a) * 0.15)) >= float(b):
                                try:
                                    difference = abs(float(a) - float(b))
                                    percent = (difference / float(b)) * 100
                                    send_email_alert(name['nome'], price_file['link'], b, "{:.1f}%".format(percent))
                                except:
                                    pass


def refresh_token():
    credentials = ('3ba13a6c-e200-4e7c-ace1-b17f47f410df',
                   '_lr8Q~-6NPRbD2CU4zszbZMfMkrki7IE5zRKCbau')
    token_backend = FileSystemTokenBackend(
        token_path=os.path.join(os.getcwd(), 'Conf_app'), token_filename='o365_token.txt'
    )
    account = Account(credentials, token_backend=token_backend)
    if not account.is_authenticated:
        account.authenticate(scopes=['basic', 'message_all'])

    connection = Connection(credentials, token_backend=token_backend, scopes=[
                            'basic', 'message_all'])
    connection.refresh_token()

    print("Outlook autenticado.")
    return account

def send_email_alert(produto, loja, valor, porcentagem):
    loja2 = loja.split('.')[1]
    account = refresh_token()
    if account.is_authenticated == True:
        m = account.new_message()
        m.to.add('cowlfnt@gmail.com')
        m.subject = f'Alerta de preço – {loja2} / R${valor} / {porcentagem}'
        body = f"""
            <html>
                <body>
                    <center><h1>Relatório do Robô Dermage Product Search</h1></center>
                    <p>Produtos: {produto}</p>
                    <p>Loja: {loja2}</p>
                    <p>Link: {loja}</p>
                    <p>Valor: R${valor}</p>
                    <p>Porcentagem: {porcentagem}</p>
                </body>
            </html>"""
        m.body = body
        m.send()
        print('Email Enviado')
    else:
        print('Outlook não conectado')


def build_json(dermage, jsons):
    for json in jsons:
        archive = open_archive_json(json)
        for lojas in archive['lojas']:
            dermage['lojas'].append(lojas)
        for precos in archive['precos']:
            dermage['precos'].append(precos)
    return dermage


def create_json(file):
    with open('../frontend/json/geral.json', 'w') as archive:
        json.dump(file, archive)


def start():
    file_dermage = read_json_dermage(folder_jsons())
    dermage = open_archive_json(file_dermage)
    jsons = get_json_geral(folder_jsons())
    file = build_json(dermage, jsons)
    alert_price(dermage, jsons)
    create_json(file)


start()
