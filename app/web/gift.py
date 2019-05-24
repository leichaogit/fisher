from _curses import flash

from flask import current_app
from flask.ext.login.utils import login_required, current_user
from flask.templating import render_template

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
        try:
            gift = Gift()
            gift.isbn = isbn
            # current_user:实例化当前用户的模型
            gift.uid = current_user.id
            if current_user.beans >= current_app.config['BEANS_USE_NUMBER']:
                current_user.beans -= current_app.config['BEANS_USE_NUMBER']
            else:
                flash("您当前的鱼豆数量不足，请充值！")
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    else:
        flash('这本书已经添加到赠送或者礼物清单，请不要重复添加')
    return render_template('gifts.html', recent={'book': {}})


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    pass
