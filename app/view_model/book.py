class BookViewModel:
    """对单本书籍的数据进行处理"""

    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.author = book['author']
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushubook, keyword):
        """
        对接收的url信息进行处理
        :param yushubook:
        :param keyword:
        :return:
        """
        self.total = yushubook.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushubook.books]


class _BookViewModel:
    """
    伪类，封装的是面对过程，
    """
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        """
        对接收到的书籍数据进行处理
        :param data:
        :return:
        """
        book = {
            "title": data["title"],
            "publisher": data["publisher"],
            "pages": data["pages"] or '',
            "author": data["author"],
            "price": data["price"],
            "summary": data["summary"] or '',
            "image": data["summary"]
        }
        return book
