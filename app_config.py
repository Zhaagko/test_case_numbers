from dotenv import load_dotenv
from os import environ

load_dotenv(".env")


class AppConfig:
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']


class TelegramDeliveriesBotConfig:
    BOT_TOKEN = environ['TELEGRAM_DELIVERIES_BOT_TOKEN']


class DeliveriesDB:
    UPDATE_FREQ = 100
