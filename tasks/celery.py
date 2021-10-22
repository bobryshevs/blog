from celery import Celery
from dotenv import dotenv_values

config = dotenv_values('.env')

broker_uri = f"amqp://{config['RABBITMQ_DEFAULT_USER']}" \
    f":{config['RABBITMQ_DEFAULT_PASS']}@{config['RABBITMQ_HOST']}" \
    f":{config['RABBITMQ_PORT']}//"

app = Celery(
    main=__name__,
    broker=broker_uri,
    backend="rpc://"
)
app.autodiscover_tasks(force=True)
