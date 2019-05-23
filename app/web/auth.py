from flask import redirect
from flask import request, flash
from flask import url_for
from flask.templating import render_template
from app.forms.auth import RegisterForm, LoginForm
from app.models import db
from app.models.user import User
from . import web

__author__ = '慕言'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        # 利用了python的动态赋值特性
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return render_template('index.html')
        # return redirect(url_for('web.index'))
    return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            return render_template('index.html')
        else:
            flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


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
