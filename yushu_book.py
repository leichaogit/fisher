from app.libs.httptest import Http
from app.setting import PER_PAGE


class YuShuBook:
    search_by_isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    search_by_key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.search_by_isbn_url.format(isbn)
        return Http.get(url)

    @classmethod
    def search_by_key(cls, p, page):
        url = cls.search_by_key_url.format(p, PER_PAGE, cls.count_page(page))
        return Http.get(url)

    @classmethod
    def count_page(cls, page):
        start = (page - 1) * PER_PAGE
        return start
