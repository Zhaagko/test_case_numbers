from flask import Flask
# Blueprints
from apps.controller import module


def create_app():
    app = Flask(__name__)

    app.register_blueprint(module)

    return app
