from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import func


db = SQLAlchemy()

class BaseModel(object):
    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True)

class TimestampModel(object):
    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, nullable=False, default=func.now())