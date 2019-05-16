from flask import jsonify

from helper import is_key_or_isbn
from yushu_book import YuShuBook
from . import books
@books.route('/book/search/<p>/<page>')
def search(p, page):
    """
    搜索书籍的路由
    get
    :param p: isbn or key
    :param page: 页码
    :return:
    """
    key_or_isbn = is_key_or_isbn(p)
    if key_or_isbn == 'key':
        # 从查询关键字的接口进行查询
        result = YuShuBook.search_by_key(p,page)
    else:
        # 从isbn的接口进行查询
        result = YuShuBook.search_by_isbn(p)
    return jsonify(result)
@books.route('/')
def index():
    return 'hello word!'