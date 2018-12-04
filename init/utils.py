import jwt
import hashlib
from flask import current_app
from datetime import datetime


def generate_jwt_token(user_id):
    iat = datetime.utcnow()
    return jwt.encode(
        {
            'user_id': user_id,
            'iat': iat,
            'exp': 
                (iat + current_app.config.get('JWT_EXPIRATION_DELTA')),
            'nbf':
                (iat + current_app.config.get('JWT_NOT_BEFORE_DELTA')),
        },
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    ).decode('utf-8')


def make_password_hash(password):
    return hashlib.md5(
        password.join(
            current_app.config['SECRET_KEY']
        ).encode('utf-8')
    ).hexdigest()


def parse_json_to_object(obj, data_json):
    fields = set(data_json.keys())
    for field in fields:
        setattr(obj, field, data_json[field])
