from bs4 import BeautifulSoup
import requests, lxml

html = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(html.text, 'lxml')

names = soup.select('.LCOyB .kKpP0n')
prices = soup.select('.HgnCe span')

title = soup.select_one('h1')
print(title.text)

for name, price in zip(names, prices):
    price(name.text, price.text)