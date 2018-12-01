from flask import Blueprint
from apps.sparks.views import *

sparks = Blueprint('sparks', __name__, url_prefix='/sparks')
sparks_view = SparkView.as_view('spark_view')


sparks.add_url_rule(
    '',
    view_func=sparks_view,
    methods=['GET']
)