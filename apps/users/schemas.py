from apps.users.models import User
from flask_jwt import current_identity
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash

from marshmallow import (
    Schema,
    fields,
    validates_schema,
    post_load,
    ValidationError,
    validates
)


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    email = fields.Email()

    @validates('email')
    def validate_email(self, email):
        try:
            user = User.query.filter(User.email == email.lower()).one()
            if user.id == current_identity.id:
                user = None
        except NoResultFound:
            user = None

        if user:
            raise ValidationError('This email already taken.')


class UserRegistrationSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

    @post_load
    def hash_password(self, in_data):
        in_data['password'] = generate_password_hash(in_data['password'])
        return in_data

    @post_load
    def lower_email(self, in_data):
        in_data['email'] = in_data['email'].lower().strip()
        return in_data

    @validates('email')
    def validate_email(self, email):
        try:
            user = User.query.filter(User.email == email.lower()).one()
        except NoResultFound:
            user = None

        if user:
            raise ValidationError('This email already taken.')

    @validates_schema
    def validate_password(self, obj):
        if len(obj['password']) < 6:
            raise ValidationError(
                'Your password must be at least 6 characters.',
                ['password', ]
            )


class UserNameUpdateSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
