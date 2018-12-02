from init.database import db, BaseModel, TimestampModel



class User(db.Model, BaseModel, TimestampModel):
    __tablename__ = "users"
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
