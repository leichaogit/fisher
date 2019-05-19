from flask import jsonify
from flask import request

from app.forms.form import SearchForms
from app.libs.helper import is_key_or_isbn
from app.view_model.book import BookViewModle
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
    # 参数校验成功
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        key_or_isbn = is_key_or_isbn(q)
        # 对后续需要渲染的数据进行处理
        if key_or_isbn == 'key':
            result = YuShuBook.search_by_key(q, page)
            result = BookViewModle.package_collection(result, q)
        else:
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModle.package_single(result, q)
        return jsonify(result)
    else:
        return jsonify(form.errors)


@web.route('/')
def index():
    return 'hello word!'
