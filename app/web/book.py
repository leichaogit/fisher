from flask import request
from flask.templating import render_template

from app.forms.form import SearchForms
from app.libs.helper import is_key_or_isbn
from app.view_model.book import BookCollection, BookViewModel
from . import web
from yushu_book import YuShuBook
from flask import flash


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
        yushubook = YuShuBook()
        if key_or_isbn == 'key':
            yushubook.search_by_key(q, page)
        else:
            yushubook.search_by_isbn(q)
        books.fill(yushubook, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        flash("收索的关键字不符合要求，请重新输入关键字")
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    """
    获取书籍数据
    对单本书籍的数据进行处理
    :param isbn:
    :return:
    """
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])
