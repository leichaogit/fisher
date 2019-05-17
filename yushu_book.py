from httptest import Http


class YuShuBook:
    # search_by_isbn_url = "http://t.yushu.im/v2/book/isbn/9787535436702"
    # http://127.0.0.1:5000/book/search?q=9787535436702&page=1
    search_by_isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    search_by_key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.search_by_isbn_url.format(isbn)
        return Http.get(url)

    @classmethod
    def search_by_key(cls, p, count=15, start=0):
        url = cls.search_by_key_url.format(p, count, start)
        return Http.get(url)
