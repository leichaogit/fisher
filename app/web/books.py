from flask import jsonify
from flask import request

from app.web import web
from helper import is_key_or_isbn
from yushu_book import YuShuBook
from app.forms.form import SearchForms


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
    # 参数校验成功过
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        # q = request.args['q']
        # page = request.args['page']
        key_or_isbn = is_key_or_isbn(q)
        if key_or_isbn == 'key':
            result = YuShuBook.search_by_key(q, page)
        else:
            result = YuShuBook.search_by_isbn(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)


@web.route('/')
def index():
    return 'hello word!'