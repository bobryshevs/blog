from commands import (
    ModelMongoCreateCommand,
    RabbitPutModelCommand,
    RedisSetPostCommand
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
    RedisSetPostCommand(None, None)
]

from collections import Counter

print(Counter(coms))