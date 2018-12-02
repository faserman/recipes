from flask import Blueprint
from apps.users.views import *

users = Blueprint('users', __name__, url_prefix='/users')
users_view = UserView.as_view("users_view")

users.add_url_rule(
    '',
    view_func=users_view,
    methods=['GET', 'POST', 'PUT']
)