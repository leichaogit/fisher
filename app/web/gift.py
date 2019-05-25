from _curses import flash

from flask import current_app
from flask import redirect
from flask import url_for
from flask.ext.login.utils import login_required, current_user

from app.models import db
from app.models.gift import Gift
from . import web

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My gift'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    """
    判断isbn是否在用户模型当中
    :param isbn:
    :return:
    """
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            # current_user:实例化当前用户的模型
            gift.uid = current_user.id
            current_user.beans -= current_app.config['BEANS_USE_NUMBER']
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    pass
