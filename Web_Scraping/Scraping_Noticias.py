import requests
from bs4 import BeautifulSoup as bs4


link = 'https://g1.globo.com'
response = requests.get(link).content
print(response)

site = bs4(response, 'html.parser')

noticia = site.find('span', class_='bstn-hl-title')
print(noticia.string)
