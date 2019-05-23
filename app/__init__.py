from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')

    # 统一注册蓝图
    from app.web import web
    app.register_blueprint(web)
    return app
