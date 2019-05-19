class BookViewModle:
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
