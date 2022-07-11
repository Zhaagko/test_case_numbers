from flask import Blueprint, render_template
from flask_restful import Resource

url_prefix = "/deliveries"

deliveries = Blueprint("deliveries", __name__, url_prefix=url_prefix)


@deliveries.route("/")
def index():
    return render_template("index.html")


class DeliveriesRest(Resource):

    def get(self):
        return {'init': 'Hello, World!'}
