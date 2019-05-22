from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    # 不创建主键
    __abstract__ = True
    # １．表示数据存在；０．表示数据已经被删除，不要使用物理删除方式
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # hasattr:判断对象是否具有某个属性，可以用来写一个简单的单利
            # setattr:向对象设置某个属性需要输入3个参数
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
