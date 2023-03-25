from bs4 import BeautifulSoup
from parsers.book_parser import Bookparser
from locater.locater import Locator


class AllBookPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [Bookparser(e) for e in self.soup.select(Locator.BOOK)]
