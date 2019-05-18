from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column

db = SQLAlchemy()


class Person(db.Model):
    id = Column(db.Integer, autoincrement=True, primary_key=True)
    title = Column(db.String(50), nullable=False)
    _author = Column('author', db.String(30), default='佚名')
    binding = Column(db.String(20))
    publisher = Column(db.String(50))
    price = Column(db.String(20))
    pages = Column(db.Integer)
    pubdate = Column(db.String(20))
    isbn = Column(db.String(15), nullable=False, unique=True)
    summary = Column(db.String(1000))
    image = Column(db.String(50))
