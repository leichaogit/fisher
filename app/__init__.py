from flask import Flask

from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')

    # 增加上下文管理器，添加入栈
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # 统一注册蓝图
    from app.web import web
    app.register_blueprint(web)
    return app


