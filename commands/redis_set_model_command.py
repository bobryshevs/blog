from models import Model
from json_serializers import JsonSerializer
from commands import ReversibleCommand


class RedisSetModelCommand(ReversibleCommand):
    def __init__(self, redis_obj, json_serializer: JsonSerializer) -> None:
        self.redis = redis_obj
        self.serializer = json_serializer
        self.model_id: str = None

    def do(self, model: Model) -> None:
        self.model_id = str(model.id)
        self.redis.set(self.model_id, self.serializer.to_json(model))

    def undo(self):
        self.redis.delete(self.model_id)
