from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr


db = SQLAlchemy()

class BaseModel(object):
    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True)