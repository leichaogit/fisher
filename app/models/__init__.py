from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    # １．表示数据存在；０．表示数据已经被删除，不要使用物理删除方式
    status = Column(SmallInteger, default=1)
