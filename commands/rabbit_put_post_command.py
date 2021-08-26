from models import Model
from commands import Command
from json_serializers import JsonSerializer


class RabbitPutModelCommand(Command):
    """ This command should be called last """

    def __init__(self, channel, json_serializer: JsonSerializer) -> None:
        self.channel = channel
        self.serializer = json_serializer

    def do(self, model: Model) -> None:
        self.channel.basic_publish(
            exchange='',
            routing_key='post',
            body=self.serializer.to_json(model))
