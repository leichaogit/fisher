from app.libs.httptest import Http
from app.setting import PER_PAGE
from flask import current_app


class YuShuBook:
    search_by_isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    search_by_key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        """
        :param isbn:
        :return:get isbn book message
        """
        url = self.search_by_isbn_url.format(isbn)
        result = Http.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books = data['books']

    def search_by_key(self, p, page):
        """
        :param p:
        :param page:
        :return:get keywords book message
        """
        url = self.search_by_key_url.format(p, current_app.config['PER_PAGE'], self.count_page(page))
        result = Http.get(url)
        self.__fill_collection(result)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def count_page(self, page):
        start = (page - 1) * PER_PAGE
        return start
