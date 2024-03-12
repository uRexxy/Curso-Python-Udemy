import requests
from bs4 import BeautifulSoup

# Identificando o Header do site
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"}

# Buscando o link do site
link = "https://www.google.com/search?q=cotação+dólar"
request = requests.get(link, headers=headers)
print(request)
site = BeautifulSoup(request.text, "html.parser")


html_cotacao_dolar = site.find("span", class_="SwHCTb")

cotacao_dolar = html_cotacao_dolar.get_text()
print(f'Um Dólar vale R${cotacao_dolar}.')
