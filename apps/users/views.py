from flask import request, jsonify
from flask.views import MethodView
from apps.users.models import User
from init.utils import generate_jwt_token, parse_json_to_object
from init.database import db
from apps.users.schemas import UserRegistrationSchema, UserSchema, UserNameUpdateSchema
from flask_jwt import current_identity, jwt_required


class UserView(MethodView):
    @jwt_required()
    def get(self):
        result = UserSchema().dump(current_identity)
        return jsonify(result.data)

    def post(self):
        json_data = request.get_json()
        result = UserRegistrationSchema().load(json_data)
        if result.errors:
            return jsonify(result.errors), 403
        user = User()
        parse_json_to_object(user, result.data)
        db.session.add(user)
        db.session.commit()
        token = generate_jwt_token(user.id)
        return jsonify({
            'token': token
        })

    @jwt_required()
    def put(self):
        json_data = request.get_json()
        result = UserNameUpdateSchema().load(json_data)
        if result.errors:
            return jsonify(result.errors), 403
        user = User.query.get(current_identity.id)
        parse_json_to_object(user, result.data)
        db.session.add(user)
        db.session.commit()
        result = UserSchema().dump(user)
        return jsonify(result.data)
