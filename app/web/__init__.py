from flask import Blueprint
# web为公共使用的蓝图对象
web = Blueprint('web', __name__)
from . import books
from . import user
