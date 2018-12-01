from init.database import db, BaseModel

class Spark(BaseModel, db.Model):
    __tablename__ = "sparks"

    name = db.Column(db.String(80))