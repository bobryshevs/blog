from translators import PostTranslator
from models import Post
from .reversible_command import ReversibleCommand


class RedisSetPostCommand(ReversibleCommand):
    def __init__(self, redis_obj, translator: PostTranslator) -> None:
        self.redis = redis_obj
        self.translator = translator

    def do(self, post: Post) -> None:
        self.redis.set(self.post_id)
