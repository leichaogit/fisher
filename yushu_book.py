from httptest import Http


class YuShuBook:
    __per_page = 15
    # search_by_isbn_url = "http://t.yushu.im/v2/book/isbn/9787535436702"
    # http://127.0.0.1:5000/book/search?q=9787535436702&page=1
    search_by_isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    search_by_key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.search_by_isbn_url.format(isbn)
        return Http.get(url)

    @classmethod
    # start = (page - 1)*cls.__per_page
    def search_by_key(cls, p, page):
        url = cls.search_by_key_url.format(p, cls.__per_page, cls.count_page(page))
        return Http.get(url)

    @classmethod
    def count_page(cls, page):
        start = (page - 1) * cls.__per_page
        return start
