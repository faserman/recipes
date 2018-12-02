from flask import request, jsonify
from flask.views import MethodView
from apps.users.models import User
from init.utils import make_password_hash, generate_jwt_token
from init.database import db

class UserView(MethodView):
    def get(self):
        return 

    def post(self):
        json_data = request.get_json()
        user = User()
        user.email = json_data['email']
        user.password = make_password_hash(json_data['password'])
        user.name = json_data['name']
        db.session.add(user)
        db.session.commit()
        token = generate_jwt_token(user.id)
        return jsonify({
            'token': token
        })

    def put(self):
        return 
