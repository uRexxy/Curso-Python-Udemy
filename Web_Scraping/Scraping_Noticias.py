import requests
from bs4 import BeautifulSoup as bs4


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'}
link = 'https://www.leroymerlin.com.br/pagina-de-ofertas-promocoes'
response = requests.get(link, headers=header)
print(response)

site = bs4(response.text, 'html.parser')

nome_produto = site.find('span', class_='enof0xo0')
print(nome_produto)
