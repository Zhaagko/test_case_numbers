from apps import create_app
from apps.global_services import create_worker

worker = create_worker()
worker.start()

if __name__ == "__main__":
    app = create_app()
    app.run()
