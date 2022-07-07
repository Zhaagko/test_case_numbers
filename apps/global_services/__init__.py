from apps.global_services.background_worker import Worker
from apps.deliveries.services import update_delivery_database


def create_worker(app):
    # Init background worker
    worker = Worker()
    # Add global tasks to worker
    worker.add_task("update_delivery_database", update_delivery_database, (app, 20))
    # Run worker
    return worker
