from flask import Flask
# App-config
from app_config import AppConfig
# Database
from apps.database import db
# Models
from apps.deliveries.models import *
# Blueprints
from apps.deliveries.controllers import deliveries
# RestApi
from apps.restapi import restapi
# Rest Resources
from apps.deliveries.rest import DeliveriesRest


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    app.register_blueprint(deliveries)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Add RestApi resources
    restapi.add_resource(DeliveriesRest, "/api")
    # Init Flask-app in RestApi
    restapi.init_app(app)

    return app
