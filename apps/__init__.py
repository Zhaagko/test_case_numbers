from flask import Flask
# App-config
from app_config import AppConfig
# Database
from apps.database import db
# Blueprints
from apps.deliveries.controllers import deliveries


def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    app.register_blueprint(deliveries)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
