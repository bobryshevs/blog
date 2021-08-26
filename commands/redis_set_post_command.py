from .reversible_command import ReversibleCommand


class RedisSetPostCommand(ReversibleCommand):
    def __init__(self, redis_obj, post_id: str, post: str) -> None:
        self.redis = redis_obj
        self.post_id: str = post_id
        self.post: str = post

    def do(self) -> None:
        self.redis.set(self.post_id)
