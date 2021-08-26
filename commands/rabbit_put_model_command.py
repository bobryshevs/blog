from models import Model
from commands import Command
from json_serializers import JsonSerializer


class RabbitPutModelCommand(Command):
    """ This command should be called last """

    def __init__(self,
                 channel,
                 json_serializer: JsonSerializer,
                 routing_key: str):
        self.channel = channel
        self.serializer = json_serializer
        self.routing_key = routing_key

    def do(self, model: Model) -> None:
        self.channel.basic_publish(
            exchange="",
            routing_key=self.routing_key,
            body=self.serializer.to_json(model))
