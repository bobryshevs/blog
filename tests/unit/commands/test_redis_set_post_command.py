from commands import RedisSetModelCommand
from mock import Mock


class TestRedisSetModelCommand:

    def setup(self):
        self.redis = Mock()
        self.serializer = Mock()
        self.model = Mock()

    def test_do(self):
        command = RedisSetModelCommand(
            redis_obj=self.redis,
            json_serializer=self.serializer
        )

        command.do(self.model)

        self.serializer.to_json.assert_called_once_with(self.model)
        self.redis.set.assert_called_once()

    def test_undo(self):
        command = RedisSetModelCommand(
            redis_obj=self.redis,
            json_serializer=self.serializer
        )
        expected_id = "ID"
        command.model_id = expected_id

        command.undo()

        self.redis.delete.assert_called_once_with(expected_id)
