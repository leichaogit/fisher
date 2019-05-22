from flask import request
from flask.templating import render_template

from app.forms.auth import RegisterForm
from app.models.user import User
from . import web

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        # 利用了python的动态赋值特性
        user.set_attrs(form.data)
        # user.password(form.password.data)
        # user.nickname = form.nickname.data
        # user.email = form.email.data
    return render_template('auth/register.html', form={'data':{}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
