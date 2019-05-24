from flask.ext.login.mixins import UserMixin
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.libs.helper import is_key_or_isbn
from app.models import Base
from app.models.gift import Gift
from yushu_book import YuShuBook


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), unique=True, nullable=False)
    _password = Column("password", String(128))
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        """
        如果要设置为只读属性，那么就不使用用户传来的属性，并抛出异常
        :param raw:
        :return:
        """
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        """
        1.判断isbn的格式
        2.判断isbn是否存在数据库中
        3.判断当前用
        :param isbn:
        :return:
        """
        if is_key_or_isbn(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 在礼物清单
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        # 在愿望清单
        wishing = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        if not gifting and not wishing:
            return True
        return False


@login_manager.user_loader
def get_user(uid):
    """
    确保uid为主键的时候，才可以这样使用
    :param uid:
    :return:
    """
    return User.query.get(int(uid))
