from flask import redirect
from flask import request, flash
from flask import url_for
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.templating import render_template
from app.forms.auth import RegisterForm, LoginForm
from app.models import db
from app.models.user import User
from app.web import web

__author__ = '慕言'


@web.route('/register', methods=['GET', 'POST'])
def register():
    """
    表单数据
    完成注册，返回登陆界面
    :return:
    """
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=False)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    """
    登陆成功，保存用户的session信息，使用flask_login模块
    :return:
    """
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # 只需要记录用户的ID,注意需要在类中继承UserMixin
            login_user(user, remember=True)
            # 跳转到原页面
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('用户名或密码错误,请重新输入！')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
@login_required
def forget_password_request():
    return 'hello world'


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
