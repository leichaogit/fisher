from flask import json
from flask import jsonify
from flask import request

from app.forms.form import SearchForms
from app.libs.helper import is_key_or_isbn
from app.view_model.book import BookCollection
from app.web import web
from yushu_book import YuShuBook


@web.route('/book/search')
def search():
    """
    搜索书籍的路由
    ?p=哈哈&page=
    :param p: isbn or key
    :param page: 页码
    :return:
    """
    # Request Response
    # HTTP请求信息
    # 查询参数 POST参数 remote ip
    form = SearchForms(request.args)
    books = BookCollection()
    # 参数校验成功
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        key_or_isbn = is_key_or_isbn(q)
        # 对后续需要渲染的数据进行处理
        yushu_book = YuShuBook()
        if key_or_isbn == 'key':
            yushu_book.search_by_key(q,page)
        else:
            yushu_book.search_by_isbn(q)
        books.fill(yushu_book,q)
        return json.dumps(books,default=lambda  o:o.__dict__)
    else:
        return jsonify(form.errors)


@web.route('/')
def index():
    return 'hello word!'
