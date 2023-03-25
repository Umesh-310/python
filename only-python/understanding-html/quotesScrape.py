import requests
from bs4 import BeautifulSoup

fullPage = requests.get('http://quotes.toscrape.com/')

# print(fullPage.content)
soup = BeautifulSoup(fullPage.content , 'html.parser')

print(soup.select_one('div.quote small.author').string)
