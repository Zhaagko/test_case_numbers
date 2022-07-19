from apps.database import db
from sqlalchemy import func
import datetime


class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(32))
    cost_usd = db.Column(db.Numeric)
    cost_rub = db.Column(db.Numeric)
    term = db.Column(db.Date)

    def __repr__(self):
        return self.number

    @staticmethod
    def get_overdue():
        return Delivery.query.filter(func.date(Delivery.term) < datetime.date.today()).all()
