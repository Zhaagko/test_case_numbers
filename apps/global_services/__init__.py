from apps.global_services.background_worker import Worker
from apps.deliveries.services import update_delivery_database
from apps.deliveries.services.telegram_bot.deliveries import run_bot
from app_config import DeliveriesDB


def create_worker(app):
    # Init background worker
    worker = Worker()
    # Add global tasks to worker
    worker.add_task("update_delivery_database", update_delivery_database, (app, DeliveriesDB.UPDATE_FREQ))
    worker.add_task("telegram_deliveries_bot", run_bot, (app, ))
    # Run worker
    return worker
