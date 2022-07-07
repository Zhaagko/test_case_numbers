from apps import create_app
from apps.global_services.background_worker import Worker

# Init background worker
worker = Worker()
# Add global tasks to worker
#
# Tasks
#
# Run worker
worker.run()

if __name__ == "__main__":
    app = create_app()
    app.run()
