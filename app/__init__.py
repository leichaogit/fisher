from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')

    login_manager.init_app(app)
    # 引导用户登陆的方法
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请'
    # 统一注册蓝图
    from app.web import web
    app.register_blueprint(web)
    return app
