def headers(categ): return {
  'authority': 'www.dermage.com.br',
  'accept': '*/*',
  'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'if-none-match': '"CA09C111155AB58EDE3D493F2A540B90"',
  'referer': f'https://www.dermage.com.br/{categ}?PS=32&sl=b7a2f291-c412-4676-ae81-82bfd7e36c33&cc=4&sm=0&PageNumber=1',
  'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26',
  'x-requested-with': 'XMLHttpRequest',
}


def params(page_number): return {
  'PS': '32',
  'sl': 'b7a2f291-c412-4676-ae81-82bfd7e36c33',
  'cc': '4',
  'sm': '0',
  'PageNumber': f'{page_number}',
}


def mount_payload(categ, page_number): return {
  'url': f'https://www.dermage.com.br/{categ}',
  'params': params(page_number),
  'headers': headers(categ)
}


paginas_categorias = {
  'rosto': 5,
  'corpo': 3,
  'cabelo': 2,
  'fotoprotecao': 2,
  'maquiagem': 3
}
