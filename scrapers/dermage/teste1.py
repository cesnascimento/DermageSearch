import requests
from bs4 import BeautifulSoup
import re
import json
import locale


dermage_session = requests.Session()
categs = ['rosto', 'corpo', 'cabelo', 'fotoprotecao', 'maquiagem']

for categ in categs:
    headers = {
        'authority': 'www.dermage.com.br',
        'accept': '*/*',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': f"_gcl_au=1.1.1614968718.1666617716; _fbp=fb.2.1666617716559.1082104585; checkout.vtex.com=__ofid=2c13797c1bb045a2ba1bb47bad9cf28f; _tt_enable_cookie=1; _ttp=27aa93b0-0446-4a0b-95de-6e0d7c9e0eab; IPI=UrlReferrer=https%3a%2f%2fduckduckgo.com%2f; xe_visitor=eyJpZCI6IjNiYmFhZGIyLTZiZGYtNGZiMS04NmQwLWIzN2Y2NmQ3ODAxNCIsImVtYWlsIjoiIn0=; AdoptVisitorId=OwYwHApsCMCcYFpoAYAsAmBqBGoG1ggDYEAzHZEYVAQwFYJoQg==; .ASPXAUTH=468C87757F26F5C50159693750EB7F70C2488B8B75985AAEEDDED126EFAA34EC55CCC48BAFC1A8ADF84265797104F02497D645284C745483FB037EC61AB681F46B9251923A6F5119DCAB1DA059AE1F2A514D3B81FC8674C17F6569612C9DA082B60ECD30983F40ED33B30272B82E6AAF6D0C811216330A0060A4C725CB932F1586441862330A0E104952551D94573376173528D343D774C3F17A9B34F86868F3FD15BAE2; vtex_segment=eyJjYW1wYWlnbnMiOm51bGwsImNoYW5uZWwiOiIxIiwicHJpY2VUYWJsZXMiOm51bGwsInJlZ2lvbklkIjpudWxsLCJ1dG1fY2FtcGFpZ24iOm51bGwsInV0bV9zb3VyY2UiOm51bGwsInV0bWlfY2FtcGFpZ24iOm51bGwsImN1cnJlbmN5Q29kZSI6IkJSTCIsImN1cnJlbmN5U3ltYm9sIjoiUiQiLCJjb3VudHJ5Q29kZSI6IkJSQSIsImN1bHR1cmVJbmZvIjoicHQtQlIiLCJjaGFubmVsUHJpdmFjeSI6InB1YmxpYyJ9; sback_client=58addd0258791046b42f5bf1; sback_partner=false; sback_customer={2wdyMTTjRlSOtmMGtGRUVVTHNDcnlDRy1kR1kVR4R1YOR3aqZUWElkWtlWbGp1Vzp1UxYXR6REVal2MZ1EaysUT2$12;} sb_days=1666617721198; VtexRCMacIdv7=23ca19c0-7dba-420c-bc19-c071e3395574; _hjSessionUser_1485996=eyJpZCI6IjQ4NDIwOWEwLTQyNWItNTAxZi1iNWUxLTZkZmEzNjAwMWMxOCIsImNyZWF0ZWQiOjE2NjY2MTc3MTY4ODAsImV4aXN0aW5nIjp0cnVlfQ==; AdoptConsent=N4Ig7gpgRgzglgFwgSQCIgFwigJghAEwGYBjATgFoccBGGigFgAYAOFigQwFYOoKmCLGjgBmLAGwsGIqCAA0IAPYAHBMgB2AFQ4BzGJgDaIJlCYB2KAwJmKZrkQiMIZkRRYEGDCuKgjr4hnFnMyJ5EAtWBhIg7yJxDkYSEiYKKCgCcTdzcRESGhD4szCiDhYIGhIzBIJKr08yPjYSdjNkgg5WGhEOHAIwrmsmES47flEEwJwbd3sKERohnHEmGjIpLjCaAgIuJgZZhxNGM08KMjM8M7IOZJwhKAWGMLIiBjMdkRSyHaJGKDIUuk0pwGKYRGYzCxPgwWM93EFLAkRDgoJkGGR8Kk6PQpOIyDkiCJAkMwgQmDgiBCoFwzgQIDSGD0CKlknwMiMOGYyDweLIFCwcB1xAFmVUIDhGDQWI0GER2EsgjQiFxpOI5WEfDICETHEQoCQGVUSG5yr9xPlxAQAeZKRwwsw9VFxBLulJGBwpW58r8ICxWuTyX4VSAALoKFQIADyAFcENo9IYQwBfIA=; _hjSessionUser_1893063=eyJpZCI6ImQ4MDFjYjYxLTdjMDEtNTliYS1hM2VjLTNlMGUyZmE0NzI4MCIsImNyZWF0ZWQiOjE2NjY2MTc3NzI3NzIsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=10507b15e163d889:T=1667236958:S=ALNI_MbGD_KNHPw5d484bpZktVMGV9OgmQ; __gpi=UID=000009d014362df7:T=1667236958:RT=1667236958:S=ALNI_MbnbRNTQwwu48GVWHFLvr6U9s0jMg; cto_bundle=XrXvEF9hSUI4OXAxTkZaJTJGS2QyUm5aaVRncTJ2c3VuSWcyUUsyeHFzcSUyRkx6dHNlb0Y5ekpHT3k1SnRqZ1F5ZHV2RWNSb1pvc1k0VEVKJTJCUDB4JTJGMHUzSmN0bWZoSENxWVNXZmZHdFNSanJTQWZKVWtpYmZmanklMkZDTXRCODdoZmVlZVdONmZZaEpWbXN4dkRwQXoyUTlid082Wm5BJTNEJTNE; cto_bidid=3BEk4V9BS1RtRTdXSUZjR0lmZlBQcktoaXh1Q2JTJTJGV0gxcFZaTXFxV210dVNkUk1KQTBpOUIzWGl4V0dicGl6RGRzc2R3MldkT2M3bDB0eEV5Y2ZaUEIwJTJGWVdWYnZXWmpEb3VrOWlUcnRVbkcwWjJkWHpvcHd5YjZUU01BSmVnanFNbDc; cto_dna_bundle=7Ua_c180M0RITmhlJTJCZkMwOUJGQlhaMUN2czNrYWRsM1JvYzhJdHZjcnRMWGZidHNQTlBhYlF6OHByR0k0eWJLZjQ0QmQ; _gid=GA1.3.1606641571.1667482584; xe_config=Mzk4MzRIVDA5MCxBRUExQjRGRi04MDUyLTU0NTYtREZEMi0wMzlGRjY3OTZEOUUsZGVybWFnZS5jb20uYnI=; vtex_session=eyJhbGciOiJFUzI1NiIsImtpZCI6IkZDRTk2NEE1QTI1OTlBRUI2NEZFRTMzNzdGNTM4NUU0RUJCRTg2N0IiLCJ0eXAiOiJqd3QifQ.eyJhY2NvdW50LmlkIjoiMWExZDBhYzgtZTQ2Ni00MWQyLTlkMDMtYTQ0OWQ0ZDE3YjEyIiwiaWQiOiI3Mjc2NDdiZi1hNTNmLTQxZDQtOTQxZC1hODNlMWM5YjJhZDAiLCJ2ZXJzaW9uIjoyLCJzdWIiOiJzZXNzaW9uIiwiYWNjb3VudCI6InNlc3Npb24iLCJleHAiOjE2NjgxNzM3ODUsImlhdCI6MTY2NzQ4MjU4NSwiaXNzIjoidG9rZW4tZW1pdHRlciIsImp0aSI6ImQ0MWVmNjJiLWM5YzctNDI1Ny1hNDc2LWUwZDMwYzA4OWFjNyJ9.RAK0oZBk-uViEToGwlBj15CXpQaqsU3y20GO2DtqTY-DLaq6VqNsCuh1HvEVJQ9M325SEQAmtNdI3WRZohAyAQ; _cm_ads_activation_retry=false; VtexRCSessionIdv7=1dbb0c00-1eb6-4abb-af7b-46ab6f00864e; VTEXSC=sc=1; ISSMB=ScreenMedia=0&UserAcceptMobile=False; SGTS=14E197F5DCBA97ECDC5106F50E855D56; _hjIncludedInSessionSample=0; _hjSession_1485996=eyJpZCI6ImZlZDdiMTA2LTNiYzEtNDdhYy04OWZlLTgzYmQxZGI1ODVmYyIsImNyZWF0ZWQiOjE2Njc1NTk3NjM0NjQsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _st_ses=4588622039703927; sback_refresh_wp=no; sback_current_session=1; sback_total_sessions=15; sback_customer_w=true; sback_browser=0-64921000-16675618364c91949f4aea79f006ea5eb66bffaef4fcb362d917508792906364f96c9e80a1-56043956-200142107250,1515837167-1667561836; sback_access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuc2JhY2sudGVjaCIsImlhdCI6MTY2NzU2MTgzNywiZXhwIjoxNjY3NjQ4MjM3LCJhcGkiOiJ2MiIsImRhdGEiOnsiY2xpZW50X2lkIjoiNThhZGRkMDI1ODc5MTA0NmI0MmY1YmYxIiwiY2xpZW50X2RvbWFpbiI6ImRlcm1hZ2UuY29tLmJyIiwiY3VzdG9tZXJfaWQiOiI2MzU2OTE3ODA5MTVkMWRiYWU1MWQ3YzMiLCJjdXN0b21lcl9hbm9ueW1vdXMiOnRydWUsImNvbm5lY3Rpb25faWQiOiI2MzU2OTE3ODA5MTVkMWRiYWU1MWQ3YzQiLCJhY2Nlc3NfbGV2ZWwiOiJjdXN0b21lciJ9fQ.u1ohSoGVV3h4yJ0k6MjeOi9j5_nqan66o2EYideD9ZM.WrWruyuyEiDruyWriYKqEi; _st_no_user=1; _sptid=1895; _st_no_convert=1; _st_no_script=1; _hjSession_1893063=eyJpZCI6IjJmOTgxOTFhLWY1MzktNDEyZS05NmVlLTY4Y2RjZjY5NTIwNSIsImNyZWF0ZWQiOjE2Njc1NjE4NDQ5MDksImluU2FtcGxlIjpmYWxzZX0=; _ga_71VGXD9JNS=GS1.1.1667559762.22.1.1667562591.0.0.0; _ga=GA1.1.1739290260.1666617716; urlLastSearch=http://www.dermage.com.br/rosto?PS=32&sl=b7a2f291-c412-4676-ae81-82bfd7e36c33&cc=4&sm=0&PageNumber=1&lid=a837ba31-078b-4317-90fb-4cee4bbc9390; janus_sid=f7638220-6d71-4df2-b7b8-abddbe132f7a",
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
    for i in range(0,5):
        params = {
            'PS': '32',
            'sl': 'b7a2f291-c412-4676-ae81-82bfd7e36c33',
            'cc': '4',
            'sm': '0',
            'PageNumber': f'{i}',
        }
        n = 0
        dermage = dermage_session.get(f'https://www.dermage.com.br/{categ}', params=params, headers=headers)
        soup = BeautifulSoup(dermage.text, 'html.parser')
        skus = soup.find_all('span', 'skuProd')
        print(i)
        print(categ)
        print(skus)