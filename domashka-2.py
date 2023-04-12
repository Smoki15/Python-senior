from bs4 import BeautifulSoup
import requests, lxml

html = requests.get("https://kurs.com.ua/ru/valyuta/usd")
soup = BeautifulSoup(html.text, 'lxml')

names = soup.select('.condensed')
price = soup.select('.course')
names = soup.select('.text-right-767')


title = soup.select_one('h1')
print(title.text)

for name, price in zip(names, price):
    print(name.text, price.text)
