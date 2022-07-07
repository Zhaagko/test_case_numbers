from apps import create_app
from apps.global_services import create_worker

app = create_app()

worker = create_worker(app)
worker.start()

if __name__ == "__main__":
    app.run()
