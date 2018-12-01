from flask import jsonify, request
from flask.views import MethodView
from apps.sparks.models import Spark

class SparkView(MethodView):
    def get(self):
        spark = Spark.query.get(2)
        return jsonify({
            'result': spark.name
        })