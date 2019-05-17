from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # 统一注册蓝图
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
