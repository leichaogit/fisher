from flask import Blueprint
# web为公共使用的蓝图对象
web = Blueprint('web', __name__)
from app.web import auth
from app.web import book
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish

