'''
Each book : div.page_inner section li.col-xs-6
Name : artical.product_pod h3 a
Link : artical.product_pod h3 a
price : artical.product_pod p.price_color
Rating : article.product_pod p.star-rating
'''
import requests
import logging
from pages.all_books_page import AllBookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H%:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt',
                    )

logger = logging.getLogger('scraping')

logger.info('Loading books list....')

page_Content = requests.get('http://books.toscrape.com').content
page = AllBookPage(page_Content)
books = page.books


for i in range(2, 51):
    page_Content = requests.get(
        f'http://books.toscrape.com/catalogue/page-{i}.html').content
    page = AllBookPage(page_Content)
    books.extend(page.books)

for book in books:
    print(book)
