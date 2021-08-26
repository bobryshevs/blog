from bson.objectid import ObjectId
from models import Post
from json_serializers import JsonSerializer
from commands import ReversibleCommand


class RedisSetPostCommand(ReversibleCommand):
    def __init__(self, redis_obj, json_serializer: JsonSerializer) -> None:
        self.redis = redis_obj
        self.serializer = json_serializer
        self.post_id: str = None

    def do(self, post: Post) -> None:
        self.post_id = post.str_id
        self.redis.set(self.post_id)

    def undo(self):
        self.redis.delete(self.post_id)
