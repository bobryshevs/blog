from .celery import app


@app.task
def print_hi():
    return 1 + 2
