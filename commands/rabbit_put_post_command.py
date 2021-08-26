from models import Post
from commands import Command
from structure import post_tranlator


class RabbitPutPostCommand(Command):
    """ This command should be called last """

    def __init__(self, channel) -> None:
        self.channel = channel
        self.translator = post_tranlator

    def do(self, post: Post) -> None:
        self.channel.queue_declare(queue='posts')
        self.channel.basic_publish(exchange='',
                                   routing_key='post',
                                   body=self.translator.to_json_str(post))
