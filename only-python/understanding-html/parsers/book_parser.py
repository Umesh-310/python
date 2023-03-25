import re
from locater.locater import Locator


class Bookparser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<BOOK {self.name} , {self.price} , {self.rating} >'

    @property
    def name(self):
        locator = Locator.NAME
        item_link= self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = Locator.LINK
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = Locator.PRICE
        item_price = self.parent.select_one(locator).string

        pattern = '.([0-9]+\.[0-9]+)'
        match = re.match(pattern, item_price)
        # print(match.group(1))
        # return 32.32
        return float(match.group(1))

    @property
    def rating(self):
        locator = Locator.RATING
        item_rating = self.parent.select_one(locator).attrs['class']
        return item_rating[1]
