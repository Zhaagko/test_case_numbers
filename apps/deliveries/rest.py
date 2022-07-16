from flask import jsonify
from flask_restful import Resource
from apps.deliveries.models import Delivery
from apps.database import db


class DeliveriesRest(Resource):

    def get(self):
        deliveries = db.session.query(Delivery.term,
                                      db.func.count(Delivery.number),
                                      db.func.sum(Delivery.cost_usd)).group_by(Delivery.term).order_by(Delivery.term).limit(30).all()
        return jsonify([{"term": str(delivery[0]), "count": int(delivery[1]), "sum": float(delivery[2])} for delivery in deliveries])
