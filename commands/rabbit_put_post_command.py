from models.post import Post
from pika import (
    PlainCredentials,
    BlockingConnection,
    ConnectionParameters
)
from commands import Command


class RabbitPutPostCommand(Command):
    """ This command should be called last """

    def __init__(self, credentials: PlainCredentials, post: str) -> None:
        self.credentials = credentials
        self.connection_parameters = ConnectionParameters(
            'localhost',
            credentials=credentials
        )

    def do(self) -> None:
        with BlockingConnection(self.connection_parameters) as connection:
            channel = connection.channel()
            channel.queue_declare(queue='posts')
            channel.basic_publish(exchange='',
                                  routing_key='post',
                                  body=self.post)
