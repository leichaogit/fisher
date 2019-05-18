from flask import Flask

from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')

    # 增加上下文管理器，添加入栈
    db.init_app(app)
    # with app.app_context():
    db.create_all(app=app)
    # 统一注册蓝图
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
