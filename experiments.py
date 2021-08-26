from functools import reduce
from commands import (
    ReversibleCommand,
    Command,
    ModelMongoCreateCommand,
    RabbitPutModelCommand,
    RedisSetModelCommand
)
from re import I
from bson.objectid import ObjectId
from structure import redis_obj, post_repository
from translators import PostTranslator
from models import Post

post = Post()
post.id = ObjectId()
post.title = "title"
post.content = "content"
post.author_id = ObjectId()
post.comment_ids = [ObjectId() for _ in range(10)]


pt = PostTranslator()


coms = [
    ModelMongoCreateCommand(None),
    RabbitPutModelCommand(None, None),
    RedisSetModelCommand(None, None)
]


a = reduce(lambda c, x: c + 1 if isinstance(x,
           ReversibleCommand) else 0, coms, 0)
print(a)


class PyExc(Exception):
    def __init__(self, index: int, msg: str) -> None:
        super().__init__(msg, msg*2)
        self.index = index

try:
    raise PyExc(3, 'message')
except PyExc as err:
    print(dir(err))
    print(str(err))
    print(err.index)
